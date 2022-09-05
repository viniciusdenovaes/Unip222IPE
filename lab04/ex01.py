quantidade = int(input('Entre com uma quantidade: '))

contador = 0
numero = 1

while contador < quantidade:
    if numero % 2 == 0:
        contador += 1
        print(f'Numero {numero} eh par ({contador}-esimo numero impresso)')
    numero += 1

print('Estes foram todos os numeros')
