from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Recife', 'Fortaleza']

estados = ['SP', 'BH', 'BA']

#USANDO ZIP NORMAL , REPARE QUE RECIFE E FORTALEZA FICARAM DE FORA POIS NO SEGUNDO PARAMETRO SÓ EXISTEM 3 INDICES:

zip1 = zip(estados, cidades)
print(list(zip1))

#USANDO O ZIP_LONGEST CONSEGUIMOS INCLUIR OS INDICES QUE FICARAM DE FORA PASSANDO UM VALOR PARA O PARAMETRO "fillvalue"
zip2 = zip_longest(estados, cidades, fillvalue='Estado')
print(list(zip2))


