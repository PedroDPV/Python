#Com Try o código irá rodar até encontrar um error

try:
    print(a) # <- tem erro de sintáxe , então o python irá sair do try e ir pro except
except NameError as erro: #<- você pode especificar qual error você quer identificar no caso : 'NameError'
    print('Erro:',erro)
except Exception as erro: # <- Exception identifica qualquer tipo de error
    print('Ocorreu um erro inesperado')


print('Depois do Try e Except o codigo continua normalmente')
print('OBS: Você pode usar o finally no final do try para executar qualquer ação independete doq aconteça anteriormente')
