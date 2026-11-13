"""No graphics dependency. LAN: python server.py --host 0.0.0.0"""
import argparse
import socketserver
import threading
import uuid
from match import Match
from network import send_message, receive_message


class GameServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(self, address):
        super().__init__(address, Handler)
        self.match = Match()
        self.lock = threading.Lock()


class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        identity = uuid.uuid4().hex
        joined = False
        self.request.settimeout(30)
        try:
            request = receive_message(self.rfile)
            with self.server.lock:
                try:
                    if request.get('action') != 'join':
                        raise ValueError('Join the room first.')
                    self.server.match.join(identity, request.get('name'))
                    joined = True
                    response = {'state': self.server.match.view(identity)}
                except ValueError as error:
                    response = {'error': str(error), 'fatal': True}
            send_message(self.wfile, response)
            if not joined:
                return
            while True:
                request = receive_message(self.rfile)
                with self.server.lock:
                    match = self.server.match
                    error = ''
                    try:
                        action = request.get('action')
                        if action == 'ready':
                            match.ready(identity, request.get('fleet'))
                        elif action == 'attack':
                            match.attack(identity, request.get('x'), request.get('y'))
                        elif action == 'rematch':
                            match.rematch(identity)
                        elif action != 'state':
                            raise ValueError('Unknown action.')
                    except ValueError as exc:
                        error = str(exc)
                    response = {'state': match.view(identity), 'error': error}
                send_message(self.wfile, response)
        except (OSError, ValueError, ConnectionError):
            pass  # Connection ended; finally notifies the other player.
        finally:
            if joined:
                with self.server.lock:
                    self.server.match.leave(identity)
                    if not self.server.match.players:
                        self.server.match = Match()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Battleship classroom server')
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=65432)
    args = parser.parse_args()
    with GameServer((args.host, args.port)) as server:
        print(f'Server listening on {args.host}:{args.port}. Ctrl+C to stop.', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
