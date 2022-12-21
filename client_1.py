import socket


class Client():

    def __init__(self, ip, port, username):    
        self.ip = ip
        self.port = port
        self.end_point = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.usernamer = username 


    def conection(self):
        sock = self.sock
        end_point = self.end_point
        try:
            sock.connect(end_point)
            print('Conexão estabelecida!!')
        except:
            return print('Conexão não estabelecida!')

    
    def send_menssage(self):
        user = self.usernamer
        sock = self.sock
        while True:
            try:
                msg = str(input(f'<{user}>'))
                sock.send(msg.encode('utf-8'))  
            except:
                return print('Mensagem não enviada!')

            if msg == 'exit':
                sock.close()
                break


    def receive_menssage(self):
        sock = self.sock
        while True:
            try:
                msg = sock.recv(2048).decode('utf-8') 
                print(msg)    
            except:
                return print('Mensagem não recebida')
            


client = Client('127.0.0.1', 8080, 'Arthur')
client.conection()