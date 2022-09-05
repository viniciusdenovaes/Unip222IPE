palavra = input('Entre com uma string contendo apenas os termos 0 e 1: ')

# sequencia maxima encontrada ate agora
maximo = 0

# o tamanho da sequencia atual
sequencia_atual = 0

for s in palavra:
    if s == '0':
        sequencia_atual += 1
        if sequencia_atual > maximo:
            maximo = sequencia_atual
    else: # quando s == '1'
        sequencia_atual = 0

print(f'O tamanho da maior sequencia de 0s eh {maximo}')
