"""Convertendo o type de um input com Try except"""

def converte_numero(valor):
    try:
        valor = int(valor)
        return (valor)
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input ('Digite um numero para multiplicar por 2: '))

    if numero is None:
        print('Erro: isso não é um numero')
    else:
        print(numero * 2)