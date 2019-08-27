import socket
import time
HOST1 = socket.gethostbyname(socket.gethostname())
HOST = '192.168.43.153'
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
dest1 = (HOST1, PORT)
a = 1000000000000
b = 999999999999
start = time.time()
udp.sendto (str(a).encode(), dest)
start1 = time.time()
udp.sendto (str(b).encode(), dest1)
msg, cliente = udp.recvfrom(1024)
msg1, cliente = udp.recvfrom(1024)
print(msg.decode(),msg1.decode())
print(time.time() - start)
print(time.time() - start1)
udp.close()
