quantidade = int(input('Entre com uma quantidade: '))

contador = 0
numero = 2

while contador < quantidade:
    is_primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            is_primo = False

    if is_primo:
        contador += 1
        print(f'O numero {numero} eh primo ({contador}-esimo numero impresso)')
    numero += 1

print('Estes foram todos os numeros')

