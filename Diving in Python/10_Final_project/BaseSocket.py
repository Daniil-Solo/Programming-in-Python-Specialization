import socket


class BaseSocket:
    def __init__(self, address_family=socket.AF_INET, socket_type=socket.SOCK_STREAM, host=None, port=None):
        self.socket = socket.socket(address_family, socket_type)
        self.host = host if host else 'localhost'
        self.port = port

    def run(self):
        raise RuntimeError("This function should be redefined in the descendant class!")
