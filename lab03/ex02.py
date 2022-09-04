num01 = input('Entre com o primeiro numero: ')
num02 = input('Entre com o segundo numero: ')

if num01 < num02:
    menor = num01
    maior = num02
else:
    menor = num02
    maior = num01

print(f'Entre os numero {num01} e {num02}, o menor eh {menor} e o maior eh {maior}')

