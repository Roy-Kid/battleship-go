"""Teacher supplied: newline-delimited JSON; background I/O, snapshots for the UI."""
import json
import queue
import socket
import threading
import time

MAX_MESSAGE = 65536


def send_message(stream, data):
    encoded = json.dumps(data, ensure_ascii=False).encode('utf-8') + b'\n'
    if len(encoded) > MAX_MESSAGE:
        raise ValueError('Message too large.')
    stream.write(encoded)
    stream.flush()


def receive_message(stream):
    line = stream.readline(MAX_MESSAGE + 1)
    if not line:
        raise ConnectionError('Connection closed.')
    if len(line) > MAX_MESSAGE or not line.endswith(b'\n'):
        raise ValueError('Invalid message length.')
    value = json.loads(line)
    if not isinstance(value, dict):
        raise ValueError('Expected a JSON object.')
    return value


class Connection:
    def __init__(self, host, port, name):
        self.state = None
        self.error = ''
        self.fatal = False
        self.commands = queue.Queue(maxsize=8)
        self.stop = threading.Event()
        self.socket = None
        self.thread = threading.Thread(target=self._run, args=(host, port, name), daemon=True)
        self.thread.start()

    def submit(self, action, **data):
        try:
            self.commands.put_nowait({'action': action, **data})
        except queue.Full:
            self.error = 'Please wait for the server.'

    def _run(self, host, port, name):
        try:
            with socket.create_connection((host, port), timeout=5) as sock:
                self.socket = sock
                sock.settimeout(5)
                with sock.makefile('rwb') as stream:
                    send_message(stream, {'action': 'join', 'name': name})
                    while not self.stop.is_set():
                        response = receive_message(stream)
                        if response.get('state'):
                            self.state = response['state']
                        self.error = response.get('error', '')
                        if response.get('fatal'):
                            self.fatal = True
                            break
                        try:
                            command = self.commands.get(timeout=0.15)
                        except queue.Empty:
                            command = {'action': 'state'}
                        send_message(stream, command)
        except (OSError, ValueError, ConnectionError) as error:
            if not self.stop.is_set():
                self.error = f'Disconnected: {error}'
                self.fatal = True

    def close(self):
        self.stop.set()
        if self.socket:
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass
