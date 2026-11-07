"""运行：python -m unittest discover -s teaching/tests -v"""
import io
import json
import random
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'refactored'))
from board import cells, random_fleet, validate_fleet, fire, statistics
from match import Match
from network import send_message, receive_message

class RulesTests(unittest.TestCase):
    def test_random_layouts_have_nine_distinct_cells(self):
        for seed in range(100):
            fleet=validate_fleet(random_fleet(random.Random(seed)))
            occupied=[p for s in fleet for p in cells(s)]
            self.assertEqual(len(occupied),9)
            self.assertEqual(len(set(occupied)),9)

    def test_bad_fleets_rejected(self):
        fleet=random_fleet(random.Random(3))
        for invalid in ([],fleet[:2],fleet+[fleet[0]], [fleet[0]]*3):
            with self.assertRaises(ValueError): validate_fleet(invalid)
        fleet[0]['x']=-1
        with self.assertRaises(ValueError): validate_fleet(fleet)

    def test_repeated_and_out_of_range_shots_do_not_change_state(self):
        fleet=random_fleet(random.Random(0));shots={}
        x,y=cells(fleet[0])[0]
        fire(fleet,shots,x,y)
        for a,b in ((x,y),(-1,0),(10,0),(True,1),(1.2,0)):
            with self.assertRaises(ValueError): fire(fleet,shots,a,b)
        self.assertEqual(len(shots),1)

    def test_ship_sinks_on_last_cell_only(self):
        fleet=random_fleet(random.Random(0));shots={}
        for i,(x,y) in enumerate(cells(fleet[0])):
            result=fire(fleet,shots,x,y)
            self.assertEqual(result['kind'],'sunk' if i==3 else 'hit')
        self.assertEqual(statistics(shots)['score'],90)

    def new_match(self):
        m=Match();m.join('a','Alice');m.join('b','Bob')
        m.ready('a',random_fleet(random.Random(1)))
        m.ready('b',random_fleet(random.Random(2)))
        return m

    def test_server_turn_and_ready_contract(self):
        m=self.new_match()
        with self.assertRaises(ValueError): m.attack('b',0,0)
        self.assertEqual(m.turn,'a')
        with self.assertRaises(ValueError): m.ready('a',random_fleet())
        m.attack('a',0,0)
        self.assertEqual(m.turn,'b')
        with self.assertRaises(ValueError): m.attack('a',1,1)
        self.assertNotIn('fleet',m.view('a')['enemy'])

    def test_full_match_score_and_two_vote_rematch(self):
        m=self.new_match()
        targets=[p for s in m.players['b']['fleet'] for p in cells(s)]
        water=next((x,y) for x in range(10) for y in range(10)
                   if (x,y) not in {p for s in m.players['a']['fleet'] for p in cells(s)})
        # B 每轮选择不同水格，确保 A 最终击沉全部三艘。
        waters=[(x,y) for x in range(10) for y in range(10)
                if (x,y) not in {p for s in m.players['a']['fleet'] for p in cells(s)}]
        for i,p in enumerate(targets):
            m.attack('a',*p)
            if m.phase=='battle': m.attack('b',*waters[i])
        self.assertEqual(m.winner,'a')
        self.assertEqual(m.view('a')['me']['score'],340)
        m.rematch('a');self.assertEqual(m.phase,'finished')
        m.rematch('a');self.assertEqual(len(m.votes),1)
        m.rematch('b');self.assertEqual(m.phase,'placement')
        self.assertEqual(m.round,2)
        self.assertEqual(m.players['a']['wins'],1)
        self.assertFalse(m.players['a']['shots'])
        with self.assertRaises(ValueError): m.rematch('a')

    def test_duplicate_names_rejected_and_disconnect_explicit(self):
        m=Match();m.join('a','Alice')
        with self.assertRaises(ValueError): m.join('b','Alice')
        m.join('b','Bob');m.leave('a')
        self.assertEqual(m.view('b')['phase'],'disconnected')

class FramingTests(unittest.TestCase):
    def test_unicode_stars_and_multiple_messages(self):
        stream=io.BytesIO()
        send_message(stream,{'name':'小*船'});send_message(stream,{'x':3})
        stream.seek(0)
        self.assertEqual(receive_message(stream),{'name':'小*船'})
        self.assertEqual(receive_message(stream),{'x':3})
        with self.assertRaises(ConnectionError): receive_message(stream)

    def test_partial_transport_chunks_are_reassembled_by_reader(self):
        class Chunks(io.RawIOBase):
            def __init__(self,data): self.data=bytearray(data)
            def readable(self): return True
            def readinto(self,b):
                if not self.data: return 0
                n=min(3,len(b),len(self.data));b[:n]=self.data[:n];del self.data[:n];return n
        message={'name':'舰*船','action':'attack','x':3}
        with io.BufferedReader(Chunks((json.dumps(message,ensure_ascii=False)+'\n').encode())) as stream:
            self.assertEqual(receive_message(stream),message)

    def test_bad_messages_rejected(self):
        for value in (b'{}',b'[]\n',b'x'*65537+b'\n'):
            with self.assertRaises(ValueError): receive_message(io.BytesIO(value))

if __name__=='__main__': unittest.main()
