quantidade = int(input('Entre com uma quantidade: '))

somatorio = 0

for numero in range(1, quantidade+1):
    somatorio += numero

print(f'O valor do somatorio de {1} ate {quantidade} eh {somatorio}')
