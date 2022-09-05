numero = int(input('Entre com um numero inteiro: '))

somatorio_divisores = 0

for i in range(1, numero):
    if numero % i == 0:
        somatorio_divisores += i

if numero == somatorio_divisores:
    print(f'O numero {numero} eh perfeito')
else:
    print(f'O numero {numero} nao eh perfeito')


