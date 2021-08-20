import socket
import asyncio


class BaseSocket:
    def __init__(self, address_family=socket.AF_INET, socket_type=socket.SOCK_STREAM, host=None, port=None):
        self.socket = socket.socket(address_family, socket_type)
        self.host = host if host else 'localhost'
        self.port = port
        self.main_loop = asyncio.get_event_loop()

    async def send_data(self, some_socket, data):
        raise NotImplementedError

    async def listen_socket(self, listened_socket=None):
        raise NotImplementedError

    def set_up(self):
        raise NotImplementedError

    async def main(self):
        raise NotImplementedError

    def start(self):
        self.main_loop.run_until_complete(self.main())
