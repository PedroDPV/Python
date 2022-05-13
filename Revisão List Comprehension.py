l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1)

# EXEMPLO 1:
duplicar_l1 = [v * 2 for v in l1]
print(duplicar_l1)

# EXEMPLO 2:
exemplo2 = [(v, v2) for v in l1 for v2 in range(3)]
print(exemplo2)

# EXEMPLO 3:
l2 = ['Pedro', 'Mateus', 'João']
print(l2)
exemplo3 = [nome.replace('a', '@').upper() for nome in l2]
print(exemplo3)

# EXEMPLO 4:
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
exemplo4 = [(y, x) for x, y in tupla]
print(exemplo4)
exemplo4 = dict(exemplo4)
print(exemplo4)
print(exemplo4['valor'])

# EXEMPLO 5:
l3 = list(range(100))
print(l3)

divisiveis_por_3_e_8 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(f'os números divisíveis por 3 e 8 ao mesmo tempo da l3 são os :{divisiveis_por_3_e_8}')

# EXEMPLO 6:
nao_divisiveis_por_3 = [v if v % 3 == 0 else  'Não é divisivel por 3' for v in l3]
print(nao_divisiveis_por_3)
