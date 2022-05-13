from itertools import combinations, permutations, product

pessoas = ['Pedro', 'Mateus', 'João', 'Maria', 'Mayana', 'José', 'Miguel']

#As Combinações não se repetem:
for grupo in combinations(pessoas, 2):
    print(grupo)


print('#'*80)


#Permutation as combinações irão se repetir e aparecerão em ordem:
for grupo in permutations(pessoas, 2):
    print(grupo)

print('#'*80)


#Em products mostra todas as combinações possives determinando a quantidade de valores combinados, que no caso são 2:

for grupo in product(pessoas, repeat=2):
    print(grupo)



