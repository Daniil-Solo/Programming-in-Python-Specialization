from BaseSocket import BaseSocket


class ClientSocket(BaseSocket):
    def __init__(self, host=None, port=None):
        super().__init__(host=host, port=port)

    def run(self):
        self.socket.connect((self.host, self.port))

        message = input('Request: ')
        while message != 'stop':
            self.socket.send(message.encode())
            data = self.socket.recv(1024).decode()
            print(data)
            message = input('Request: ')
        self.socket.close()


if __name__ == "__main__":
    client = ClientSocket(host='localhost', port=10001)
    client.run()
