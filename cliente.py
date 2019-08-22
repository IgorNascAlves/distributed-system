import socket
import time
HOST1 = '192.168.43.228'  # Endereco IP do Servidor
HOST = '192.168.43.180'  
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
dest1 = (HOST1, PORT)
print ('Para sair use CTRL+X\n')
#msg = input()
a = 1009000000
#while msg != '\x18':
inicio = time.time()
udp.sendto (str(a).encode(), dest)    
msg1, cliente = udp.recvfrom(1024)
    
udp.sendto (str(a).encode(), dest1) 
msg2, cliente2 = udp.recvfrom(1024)
    
print(msg1.decode(),msg2.decode())

resp = int(msg1.decode(),base=10) + int(msg2.decode(),base=10)
print(resp)
    #msg = input()
fim = time.time()
print("tempo: ", fim - inicio)
udp.close()
