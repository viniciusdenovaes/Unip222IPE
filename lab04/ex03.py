numero = int(input('Entre com um numero inteiro: '))

is_primo = True

for divisor in range(2, numero):
    if numero % divisor == 0:
        is_primo = False

if is_primo:
    print(f'O numero {numero} eh primo')
else:
    print(f'O numero {numero} nao eh primo')

