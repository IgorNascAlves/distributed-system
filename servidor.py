import socket
import time
#HOST = '192.168.43.228'              # Endereco IP do Servidor
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    print (cliente, msg.decode())
    b = int(msg.decode() , base=10)
    print (b)
    for c in range( 0 , b, 1):
        c
    print("FIM")
    udp.sendto(str(c).encode(),cliente)
udp.close()
