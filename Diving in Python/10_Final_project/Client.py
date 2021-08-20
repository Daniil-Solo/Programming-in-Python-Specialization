import argparse
import asyncio

from BaseSocket import BaseSocket


class ClientSocket(BaseSocket):
    def __init__(self, host=None, port=None):
        super().__init__(host=host, port=port)

    def set_up(self):
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(False)

    async def listen_socket(self, listened_socket=None):
        while True:
            data = await self.main_loop.sock_recv(self.socket, 1024)
            data = data.decode()
            print(data)

    async def send_data(self, some_socket=None, data=None):
        while True:
            data = await self.main_loop.run_in_executor(None, input)
            if data == "stop":
                self.main_loop.stop()
                self.socket.close()
                return
            await self.main_loop.sock_sendall(self.socket, data.encode())

    async def main(self):
        listening_task = self.main_loop.create_task(self.listen_socket())
        sending_task = self.main_loop.create_task(self.send_data())
        await asyncio.gather(listening_task, sending_task)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost', type=str)
    parser.add_argument('--port', default=10001, type=str)
    args = parser.parse_args()
    client = ClientSocket(host=args.host, port=args.port)
    client.set_up()
    client.start()
