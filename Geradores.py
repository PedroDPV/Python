import time
import sys

def gerador():
    for n in range(10):
        yield n
        time.sleep(0.1)

print(gerador())

g = gerador()
for i in g:
    print(i)


#APLICAÇÃO PRATICA : UM GERADOR OCUPA MUITO MENOS ESPAÇO NA MEMÓRIA , COMO VOCÊ PODE VER NO EXEMPLO A SEGUIR:

l1 = [numero for numero in range(10000)]
print(f'{sys.getsizeof(l1)} bytes')


# pra criar um gerador use "()" em vez de "[]"

l2 = (numero for numero in range(10000))
print(f'{sys.getsizeof(l2)} bytes')


