import socket
import time
from BaseSocket import BaseSocket


class ServerSocket(BaseSocket):
    error_message = "error\nwrong command\n\n"
    ok_message = "ok\n\n"

    def __init__(self, host=None, port=None):
        super().__init__(host=host, port=port)
        self.storage = dict()  # {'key': [(value, timestamp),]}

    def set_up(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(socket.SOMAXCONN)
        self.socket.setblocking(False)
        print("Server is listening")

    async def send_data(self, client_socket, data):
        await self.main_loop.sock_sendall(client_socket, data)

    async def listen_socket(self, listened_socket=None):
        while True:
            try:
                request = self.main_loop.sock_recv(listened_socket, 1024).decode()
                print('Received from client: ' + request)
                response = self.get_response(request)
                await self.send_data(listened_socket, response.encode())
            except ConnectionResetError:
                break

    async def accept_sockets(self):
        while True:
            client_socket, address = await self.main_loop.sock_accept(self.socket)
            print('Connecting from', address)

            self.main_loop.create_task(self.listen_socket(client_socket))

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())

    def get_response(self, request: str) -> str:
        try:
            command = request[:3]
            if command == 'get':
                if request[4] == '*':
                    print('Requesting all data')
                    output_data = self.get_all_data()
                else:
                    key = request[4:-2]
                    print('Requesting data with key:', key)
                    output_data = self.get_data_with_key(key)
                if output_data:
                    print('Successful')
                response = 'ok\n' + output_data + '\n'
            elif command == 'put':
                input_data = request[4:-2]
                response = self.save_input_data(input_data)
            else:
                print('Unknown command ' + command)
                response = ServerSocket.error_message
            return response
        except IndexError:
            print('Too short request ' + request)
            return ServerSocket.error_message

    def get_all_data(self) -> str:
        response = ''
        for key in self.storage:
            key_data = self.get_data_with_key(key)
            response += key_data
        return response

    def get_data_with_key(self, key: str) -> str:
        key_data = ''
        try:
            values = self.storage[key]
            for value, timestamp in values:
                key_data += ' '.join([key, value, timestamp]) + '\n'
        except KeyError:
            print('Non-existing key ' + key)
        finally:
            return key_data

    def save_input_data(self, data: str) -> str:
        try:
            value_list = data.split(' ')
        except ValueError:
            print('Invalid request ' + data)
            return ServerSocket.error_message
        if len(value_list) == 2:
            key, value = value_list[0:2]
            timestamp = str(int(time.time()))
        elif len(value_list) == 3:
            key, value, timestamp = value_list
        else:
            print('Too many or too few arguments:' + data)
            return ServerSocket.error_message
        try:
            float(value)
        except ValueError:
            print('Invalid value ' + value)
            return ServerSocket.error_message
        try:
            int(timestamp)
        except ValueError:
            print('Invalid timestamp' + timestamp)
            return ServerSocket.error_message
        if key in self.storage:
            self.storage[key].append((value, timestamp))
        else:
            self.storage[key] = [(value, timestamp)]
        print('Saving:', key, value, timestamp)
        return ServerSocket.ok_message


if __name__ == "__main__":
    server = ServerSocket(port=10001)
    server.set_up()
    server.start()
