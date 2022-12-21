import socket
import threading



class Server():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.end_point = (ip, port)

    def Conection(self, server, end_point):
        server = self.server_tcp
        end_point = self.end_point

        server.bind(end_point)
        server.listen()

        

    def receive_menssage(self, server):
        server = self.server_tcp
        clients = list()

        while True:
            client, addr = server.accept()
            print(f'Conexão feita por {addr}')

            while True:
                msg = addr.recv(2048)
                print(f'{addr}: {msg.decode()}')
                if not msg:
                    break



Conection()