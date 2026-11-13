"""Match rules shared by the server and solo mode; callers handle locking."""
from board import validate_fleet, fire, statistics


class Match:
    def __init__(self):
        self.players = {}
        self.phase = 'lobby'
        self.turn = None
        self.winner = None
        self.round = 1
        self.log = []
        self.votes = set()

    def join(self, identity, name):
        if len(self.players) >= 2 or self.phase != 'lobby':
            raise ValueError('Room is full. Wait for both players to leave.')
        if not isinstance(name, str) or not name.strip() or len(name) > 16:
            raise ValueError('Name must contain 1 to 16 characters.')
        if any(p['name'] == name for p in self.players.values()):
            raise ValueError('This name is already in use.')
        self.players[identity] = {'name': name, 'fleet': [], 'shots': {}, 'ready': False, 'wins': 0}
        if len(self.players) == 2:
            self.phase = 'placement'

    def ready(self, identity, fleet):
        if self.phase != 'placement' or self.players[identity]['ready']:
            raise ValueError('Fleet is already locked or placement is unavailable.')
        self.players[identity]['fleet'] = validate_fleet(fleet)
        self.players[identity]['ready'] = True
        if all(p['ready'] for p in self.players.values()):
            self.phase = 'battle'
            self.turn = list(self.players)[(self.round - 1) % 2]
            self.log = ['Battle started.']

    def attack(self, identity, x, y):
        if self.phase != 'battle' or self.turn != identity:
            raise ValueError('Wait for your turn.')
        enemy = next(i for i in self.players if i != identity)
        player = self.players[identity]
        result = fire(self.players[enemy]['fleet'], player['shots'], x, y)
        self.log.append(f"{player['name']}: {chr(65+x)}{y+1} — {result['kind']}")
        self.log = self.log[-4:]
        if statistics(player['shots'])['sunk'] == 3:
            self.phase, self.winner, self.turn = 'finished', identity, None
            player['wins'] += 1
        else:
            self.turn = enemy
        return result

    def rematch(self, identity):
        if self.phase != 'finished':
            raise ValueError('Finish the current battle first.')
        self.votes.add(identity)
        if len(self.votes) == 2:
            for p in self.players.values():
                p.update(fleet=[], shots={}, ready=False)
            self.round += 1
            self.phase, self.winner, self.turn = 'placement', None, None
            self.votes.clear()
            self.log = []

    def leave(self, identity):
        if identity in self.players:
            del self.players[identity]
            self.phase, self.turn = 'disconnected', None

    def view(self, identity):
        me = self.players[identity]
        other_id = next((i for i in self.players if i != identity), None)
        other = self.players.get(other_id)
        def summary(p, pid):
            stats = statistics(p['shots'])
            stats['score'] += 100 if self.winner == pid else 0
            return {'name': p['name'], 'ready': p['ready'], 'wins': p['wins'], **stats}
        return {'phase': self.phase, 'round': self.round, 'my_turn': self.turn == identity,
                'won': self.winner == identity, 'me': summary(me, identity),
                'enemy': summary(other, other_id) if other else None,
                'fleet': me['fleet'], 'shots': me['shots'],
                'incoming': other['shots'] if other else {},
                'log': list(self.log), 'rematch_votes': len(self.votes)}
