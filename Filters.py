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


#Filtrando uma Lista com List comprehension
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))


#Agora USANDO FILTER:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = filter(lambda x: x> 5, lista)
print(list(nova_lista))

#Método normal para filtrar um Dicionário:
for produto in produtos:
    if produto['Preço'] > 50:
        print(produto)

#Agora USANDO FILTER:
def filtra(produto):
    if produto['Preço'] > 50:
        return True

filtro_dicionario = filter(filtra , produtos)
print(list(filtro_dicionario))