"""Terminal message lab: start server.py, then two clients. /quit exits."""
import argparse
import socket
import threading
from network import send_message, receive_message

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', type=int, default=65433)
parser.add_argument('--name', default='Alice')
args = parser.parse_args()

# Teacher-supplied connection and receiver. Students edit the message dictionary below.
def receive(stream):
    try:
        while True:
            message = receive_message(stream)
            print(f"\n{message['name']}: {message['text']}", flush=True)
    except (OSError, ValueError, ConnectionError):
        print('Connection ended. Type /quit to exit.')

with socket.create_connection((args.host,args.port), timeout=5) as sock:
    sock.settimeout(None)
    with sock.makefile('rwb') as stream:
        threading.Thread(target=receive, args=(stream,), daemon=True).start()
        print('Connected. Send a message; /quit exits.')
        try:
            while True:
                text = input('> ')
                if text == '/quit':
                    break
                message = {'name': args.name, 'text': text}
                send_message(stream, message)
        except (KeyboardInterrupt, EOFError, OSError):
            pass
        finally:
            sock.shutdown(socket.SHUT_RDWR)
