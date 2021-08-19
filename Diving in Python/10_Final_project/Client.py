import socket
from BaseSocket import BaseSocket


class ClientSocket(BaseSocket):
    def __init__(self, host=None, port=None):
        super().__init__(host=host, port=port)

    def run(self):
        self.socket.connect((self.host, self.port))

        message = input('Your message: ')
        while message != 'stop':
            self.socket.send(message.encode())
            data = self.socket.recv(1024).decode()
            print('Received from server: ' + data)
            message = input('Your message: ')
        self.socket.close()


if __name__ == "__main__":
    client = ClientSocket(host='localhost', port=10001)
    client.run()
