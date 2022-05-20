import json

dicionario = {
    'Pessoa 1': {
        'altura': 1.71,
        'peso': 70,
        'nome': 'Pedro de Paula',
        'cpf': '12345678910'
    },
     'Pessoa 2': {
        'altura': 1.50,
        'peso': 50,
        'nome': 'Mayana Maranhão',
        'cpf': '10987654321'
    }
}


for i, a in dicionario.items():
    print (i)
    for chave, valor in a.items():
        print(chave, valor)

print ("#"*50)

dicionario_json = json.dumps(dicionario, indent=True) #criando uma nova variavel pra usar seu dicionario na função json.dumps(oq voce quer converter)

print(dicionario_json)