import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.IF_INET, socket.SOCK_STREAM)
        self.server = "172.30.1.48"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

n = Network()