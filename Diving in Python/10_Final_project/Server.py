import socket
import time

from BaseSocket import BaseSocket


class ServerSocket(BaseSocket):
    error_message = "error\nwrong command\n\n"
    ok_message = "ok\n\n"

    def __init__(self, host=None, port=None):
        super().__init__(host=host, port=port)
        self.storage = dict()  # {'key': [(value, timestamp),]}

    def run(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        while True:
            client_socket, address = self.socket.accept()
            print('Connecting from', address)
            while True:
                try:
                    request = client_socket.recv(1024).decode()
                    if not request:
                        break
                    print('Received from client: ' + request)
                    response = self.get_response(request)
                    client_socket.send(response.encode())
                except ConnectionResetError:
                    break

    def get_response(self, request: str) -> str:
        try:
            command = request[:3]
            if command == 'get':
                if request[4] == '*':
                    print('key:', '*')
                    output_data = self.get_all_data()
                else:
                    key = request[4:-2]
                    print('key:', key)
                    output_data = self.get_data_with_key(key)
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
            print('Invalid request ' + data)
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
    server.run()
