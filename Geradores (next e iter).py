#Este Exercício serve para : Listas , Tuplas e Strings:

nome = 'Pedro Vasconcelos'

for letra in nome:
    print(letra)

print('#'*80)

#Transformando uma string em um Iteravel manualmente:
nome_iteravel = iter(nome)

#Usando a função next() para continuar o gerador:
print(next(nome_iteravel))
print(next(nome_iteravel))
print(next(nome_iteravel))
print(next(nome_iteravel))
print(next(nome_iteravel))

print('#'*80)

gerador = (letra for letra in nome)

for i in gerador:
    print(i)