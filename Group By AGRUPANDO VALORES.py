from itertools import groupby

alunos = [
    {'nome': 'Pedro', 'nota': 'A'},
    {'nome': 'Mateus', 'nota': 'B'},
    {'nome': 'João', 'nota': 'C'},
    {'nome': 'Mayana', 'nota': 'C'},
    {'nome': 'Eveline', 'nota': 'A'},
    {'nome': 'Miguel', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'B'},
    {'nome': 'Carol', 'nota': 'D'}
]

#ORDENANDO O DICIONÁRIO PELA NOTA: atenção!!!! o groupby só irá funcionar se os parametros estiverem ordenados

alunos.sort(key=lambda item: item['nota'])
for aluno in alunos:
    print(aluno)


print('#'*80)


#USANDO O GROUPBY CRIAREMOS OS CHAMADOS GRUPOS E PARA ACESSA-LOS , FAREMOS UM LAÇO FOR:

alunos_por_nota = groupby(alunos, lambda item: item['nota'])


for grupos, valores in alunos_por_nota:
    print(f'NOTAS : {grupos}')
    contador = 0
    for alunos_agrupados in valores:
        contador += 1
        print(f'\t{alunos_agrupados["nome"]}')

    if contador == 1:
        print(f'{contador} Aluno tirou nota {grupos}')
    else:
        print(f'{contador} Alunos tiraram nota {grupos}')




