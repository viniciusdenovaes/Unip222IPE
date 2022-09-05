quantidade = int(input('Entre com uma quantidade: '))

somatorio = 0

for i in range(quantidade):
    numero = float(input(f'Entre com o {i+1}-esimo numero: '))
    somatorio += numero

print(f'A soma dos numeros sera {somatorio}')
