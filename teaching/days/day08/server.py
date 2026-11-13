"""Teacher-supplied message server. python server.py --host 0.0.0.0"""
import argparse
import socketserver
import threading
from network import receive_message, send_message

class Room(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True
    def __init__(self, address):
        super().__init__(address, Handler)
        self.members = set()
        self.lock = threading.Lock()

class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        # One lock protects members and output streams so messages cannot interleave.
        self.request.settimeout(300)
        with self.server.lock:
            self.server.members.add(self.wfile)
        try:
            while True:
                message = receive_message(self.rfile)
                if not isinstance(message.get('name'), str) or not isinstance(message.get('text'), str):
                    raise ValueError('Expected name and text.')
                message = {'name': message['name'][:16], 'text': message['text'][:200]}
                with self.server.lock:
                    for stream in list(self.server.members):
                        try:
                            send_message(stream, message)
                        except OSError:
                            self.server.members.discard(stream)
        except (OSError, ValueError, ConnectionError):
            pass
        finally:
            with self.server.lock:
                self.server.members.discard(self.wfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=65433)
    args = parser.parse_args()
    with Room((args.host,args.port)) as server:
        print(f'Message server: {args.host}:{args.port}', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
