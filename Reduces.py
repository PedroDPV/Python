from functools import reduce
produtos = [
    {'Produto': 'p1', 'Preço': 31},
    {'Produto': 'p1', 'Preço': 100},
    {'Produto': 'p1', 'Preço': 95},
    {'Produto': 'p1', 'Preço': 78},
    {'Produto': 'p1', 'Preço': 1},
    {'Produto': 'p1', 'Preço': 54},
    {'Produto': 'p1', 'Preço': 56},
    {'Produto': 'p1', 'Preço': 21}
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Acumulando valores de uma lista normalmente:
acumula = 0
for item in lista:
    acumula += item
print(acumula)

#Agora com Reduces:
soma_lista = reduce(lambda ac, i: i + ac, lista, 0) #o acumulador do reduce está representado no parametro 'ac'
print(soma_lista)

#EXEMPLO COM IDADES :
pessoas = [
    {'Pessoa 1': 'Pedro', 'idade': 31},
    {'Pessoa 1': 'Mateus', 'idade': 10},
    {'Pessoa 1': 'João', 'idade': 95},
    {'Pessoa 1': 'Mayana', 'idade': 78},
    {'Pessoa 1': 'Eveline', 'idade': 1},
    {'Pessoa 1': 'Miguel', 'idade': 54},
    {'Pessoa 1': 'Carlos', 'idade': 56},
    {'Pessoa 1': 'Carol', 'idade': 21}
]

media_das_idades = 0

soma_das_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0) # <- Este último parametro (0) significa em qual valor inicial o acumulador (ac) do reduce irá iniciar
print(soma_das_idades)
media_das_idades = soma_das_idades / len(pessoas)
print(media_das_idades)