"""Considerando duas listas de inteiros ou floats (lista A e lista B) 
some os valores nas listas retornando uma nova lista com valores somados:

Se uma lista for maior que a outra , a soma só vai considerar o tamanho da menor.

EXEMPLO:
lista_a    =   [1, 2, 3, 4, 5, 6, 7]
lista_b    =  [1, 2, 3, 4]

======================= resultado
lista_soma = [2, 4, 6, 8]
"""

from random import randint
def numeros_aleatorios(qtd_de_numeros):
    lista = []
    for n in range(qtd_de_numeros):
        numero = randint(1, 100)
        lista.append(numero)
    return lista

lista_grande = numeros_aleatorios(10)
print(lista_grande)

lista_pequena = numeros_aleatorios(5)
print(lista_pequena)

lista = list(zip(lista_grande, lista_pequena))

soma = []
for a, b in lista:
    soma.append(a+b)

print (soma)