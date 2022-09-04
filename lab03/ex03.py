num01 = float(input('Entre com o primeiro numero: '))
num02 = float(input('Entre com o segundo numero: '))
num03 = float(input('Entre com o terceiro numero: '))

if num01 < num02:
    if num03 > num02:
        menor = num01
        maior = num03
    elif num03 < num01:
        menor = num03
        maior = num02
    else:
        menor = num01
        maior = num02
else:
    if num03 > num01:
        menor = num02
        maior = num03
    elif num03 < num02:
        menor = num03
        maior = num01
    else:
        menor = num02
        maior = num01

print(f'Entre os numero {num01}, {num02} e {num03}, o menor eh {menor} e o maior eh {maior}')

