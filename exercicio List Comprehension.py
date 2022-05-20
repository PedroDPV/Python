#USANDO LIST COMPREHENSION :
#SEPARAR EM UMA LISTA COM 5 INDÍCES DIFERENTES, CADA UM CONTENDO O CONJUNTO DE 9 DIGITOS QUE SE REPETEM NA STRING CITADA

string = '01234567890123456789012345678901234567890123456789'

#METODO NORMAL:
lista = []
for i in range(5):
    v1 = 0
    v2 = 10
    lista.append(string[v1:v2])
    v1 += 10
    v2 += 10
print(lista)
lista.clear()

#METODO COM LIST COMPREHENSION:

intervalo = 10
lista = [string[i:i+10] for i in range(0, len(string), 10)]
print(lista)

#RETORNE TODOS OS INDICES DA LISTA EM UMA STRING PORÉM AGORA SEPARADOS POR UM PONTO (".")

string2 = '.'.join(lista)
print(string2)

