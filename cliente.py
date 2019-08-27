import socket
import time
HOST1 = '192.168.0.22'  # Endereco IP do Servidor
#HOST = '192.168.43.180'
HOST = socket.gethostbyname(socket.gethostname())
#HOST = '192.168.158.1'
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
dest1 = (HOST1, PORT)
print ('Para sair use CTRL+X\n')
#msg = input()
a = 504500000
#a = 100
#while msg != '\x18':
inicio = time.time()
print("enviei servidor",dest)
udp.sendto (str(a).encode(), dest)
print("enviei servidor",dest1)
udp.sendto (str(a).encode(), dest1)

msg1, cliente = udp.recvfrom(1024)
print("recebi servidor",cliente)

msg2, cliente2 = udp.recvfrom(1024)
print("recebi servidor", cliente2)
    
print(msg1.decode(),msg2.decode())

resp = int(msg1.decode(),base=10) + int(msg2.decode(),base=10)
print(resp)
    #msg = input()
fim = time.time()
print("tempo paralelo  :", fim - inicio)
udp.close()
inicio = time.time()

for a in range(0, a*2, 1):
    a
#print(a)    
fim = time.time()
print("tempo sequencial:",fim - inicio)
