import math

print('Entre com o valor dos lados do triangulo: ')
l1 = float(input('primeiro lado: '))
l2 = float(input('segundo lado: '))

hipotenusa = math.sqrt((l1**2) + (l2**2))

print(f'O valor da hipotenusa para o triangulo de lados {l1} e {l2} sera {hipotenusa}')

