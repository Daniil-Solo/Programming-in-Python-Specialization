import socket
from BaseSocket import BaseSocket


class ServerSocket(BaseSocket):
    def __init__(self, host=None, port=None):
        super().__init__(host=host, port=port)
        self.storage = dict()

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

    @staticmethod
    def get_response(request):
        return request


if __name__ == "__main__":
    server = ServerSocket(port=10001)
    server.run()
