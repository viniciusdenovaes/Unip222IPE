l1 = int(input('Entre com o primeiro lado: '))
l2 = int(input('Entre com o segundo lado: '))
l3 = int(input('Entre com o terceiro lado: '))

if (l1 < l2+l3) and (l2 < l1+l3) and (l3 < l1+l2):
    print('O triangulo eh valido')
else:
    print('O triangulo nao eh valido')

