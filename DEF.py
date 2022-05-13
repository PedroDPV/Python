######


def saudação(saudação,nome):


    print (f'{saudação} {nome}')

    return

nome = input('Olá usuário, qual seu nome ?:')
hora = input('informe a hora:')
hora = float(hora)
if hora >=18 and hora <=24:
    saudação('boa noite',nome)
elif hora <= 18 and hora >= 12:
    saudação('boa tarde', nome)
else:
    saudação('bom dia', nome)



saudação('','')

######

def divisivel(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print(f'FIZZBUZZ! o numero {numero} é divisivel por 5 e 3 ao mesmo tempo')
    elif numero % 5 == 0:
        print(f'Buzz! o número {numero} é divisivel por 5')
    elif numero % 3 == 0 :
        print(f'Fizz! o número {numero} é divisivel por 3')
    else:
        print('esse numero não é divisivel por 3  ou 5')

    return


from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    divisivel(aleatorio)

#####

