import socket
import threading



class Server():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.end_point = (ip, port)
        self.clients = list()


    def rcv_new_conection(self, sock):
        while True:
            data = sock.recv(1024)
            if data == b'':
                sock.close()
                self.clients.remove(sock)
                return    
            print(f'<{self.addr}>{data.decode()}')
            # print(f'{data.decode()}')
            for soc in self.clients:
                if sock != soc:
                    soc.send(data)


    def conection(self):
        server = self.server_tcp
        end_point = self.end_point

        server.bind(end_point)
        server.listen()
        print('Server iniciado')

        while True:
            self.client, self.addr = server.accept()
            self.clients.append(self.client)
            th = threading.Thread(target=self.rcv_new_conection, args=[self.client])
            th.start()
            print(f'client{self.client} conectado com o endereço {self.addr}')



server = Server()

server.conection()