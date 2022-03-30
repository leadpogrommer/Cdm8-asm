import json
import threading
from queue import Queue
from typing import Callable
import sys

from websocket_server import WebsocketServer

from emulator import CDM8Emu

ws_client = None
running = True


class EmulatorThread(threading.Thread):
    def __init__(self, emu: CDM8Emu, recvq: Queue, send_message: Callable[[dict], None]):
        super().__init__()
        self.emu = emu
        self.receive_queue = recvq
        self.send_message = send_message
        self.daemon = True

    def run(self) -> None:
        self.send_state()
        while running:
            msg = self.receive_queue.get(block=True)
            if 'action' in msg.keys():
                action = msg['action']
                if action == 'step':
                    self.command_step()
        print('emulator thread stopped')

    def command_step(self):
        self.emu.step()
        self.send_state()

    def send_state(self):
        state = {
            'registers': {
                'r0': self.emu.regs[0],
                'r1': self.emu.regs[1],
                'r2': self.emu.regs[2],
                'r3': self.emu.regs[3],
                'pc': self.emu.PC,
                'sp': self.emu.SP,
                'ps': self.emu.CVZN,
            },
            'memory': self.emu.datamem
        }
        self.send_message({'action': 'state', 'data': state})


def serve(emu: CDM8Emu, port: int):
    # print(port)

    def send_message(msg: dict):
        ws_server.send_message(ws_client, json.dumps(msg))

    receive_queue = Queue()
    emu_thread = EmulatorThread(emu, receive_queue, send_message)

    def on_new_client(client, server):
        global ws_client
        if ws_client is None:
            ws_client = client
            emu_thread.start()

    def on_client_left(client, server):
        global ws_client, running
        if client == ws_client and running:
            print('client disconnected')
            running = False
            ws_server.shutdown_abruptly()

    def on_message(client, server, message):
        if client != ws_client:
            return
        receive_queue.put(json.loads(message))

    ws_server = WebsocketServer(host='127.0.0.1', port=port)
    print(ws_server.port)
    sys.stdout.flush()
    ws_server.set_fn_new_client(on_new_client)
    ws_server.set_fn_client_left(on_client_left)
    ws_server.set_fn_message_received(on_message)
    ws_server.run_forever()

    print('Server thread stopped')
