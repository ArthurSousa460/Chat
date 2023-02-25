import socket
import threading


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
            print('Conexão não estabelecida!')

        th1 = threading.Thread(target=self.send_menssage, args=[sock])
        th2 = threading.Thread(target=self.receive_menssage, args=[sock])

        th1.start()
        th2.start()



    def send_menssage(self, sock):
        user = self.usernamer
        while True:
            try:
                msg = str(input(f'<{user}>'))
                sock.send(f'{user}: {msg}'.encode('utf-8'))  
            except:
                print('Mensagem não enviada!')

            if msg == 'exit':
                sock.close()
                break


    def receive_menssage(self, sock):
        while True:
            try:
                msg = sock.recv(2048).decode('utf-8') 
                if msg == b'':
                    sock.close()
                    return
                else:
                    print(f'\r{msg}\n<{self.usernamer}>', end='')    
            except:
                return print('Mensagem não recebida')
            


client = Client()
client.conection()