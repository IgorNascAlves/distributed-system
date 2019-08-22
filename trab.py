import time

inicio = time.time()

for a in range(0, 1009000000*2, 1):
    a
print(a)    
fim = time.time()
print(fim - inicio)
