"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""
import re

def limpardigitos(cnpj):   # ESSA FUNÇÃO REMOVE DA STRING TUDO AQUILO QUE NÃO FOR DIGITOS DE 0 Á 9
    return re.sub(r'[^0-9]', '', cnpj)

def descobrir1(resposta):
    CODIGO_VALIDADOR1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digito1 = 0
    soma1 = 0
    for a in range(len(CODIGO_VALIDADOR1)):
        soma1 += int(resposta[a]) * CODIGO_VALIDADOR1[a]

    resultado1 = 11 - (soma1 % 11)

    if resultado1 > 9:
        digito1 = 0
    else:
        digito1 = resultado1
    return (digito1)

def descobrir2(resposta):
    CODIGO_VALIDADOR2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digito2 = 0
    soma2 = 0
    for a in range(len(CODIGO_VALIDADOR2)):
        soma2 += int(resposta[a]) * CODIGO_VALIDADOR2[a]

    resultado2 = 11 - (soma2 % 11)

    if resultado2 > 9:
        digito2 = 0
    else:
        digito2 = resultado2
    return (digito2)


while True:
    cnpj_informado = input('Digite o CPF que deseja validar: ')
    cnpj_informado = limpardigitos(cnpj_informado)
    print(f'O cnpj informado foi: {cnpj_informado}')

    cnpj_validado = cnpj_informado[0:-2]
    cnpj_validado = cnpj_validado + str(descobrir1(cnpj_informado)) + str(descobrir2(cnpj_informado))

    if cnpj_validado == cnpj_informado:
        print('CNPJ VÁLIDO')
    else:
        print('CNPJ INVÁLIDO!')
