#USANDO LIST COMPREHENSION :
#CALCULE O VALOR TOTAL DOS PRODUTOS

itens = []
itens.append(('Produto 1', 30))
itens.append(('Produto 2', 20))
itens.append(('Produto 3', 50))
itens.append(('Produto 4', 10))
itens.append(('Produto 5', 60))
itens.append(('Produto 6', 55))
itens.append(('Produto 7', 49))
itens.append(('Produto 8', 120))
itens.append(('Produto 9', 5.0))
itens.append(('Produto 9', '9.50'))

print(itens)

valor_total = sum([float(valor) for produto, valor in itens])
print(valor_total)
