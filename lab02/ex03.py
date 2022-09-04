import math

print('Entre com as primeiras coordenadas: ')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

resultado = math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(f'O resultado da distancia entre {(x1, y1)} e {(x2, y2)} eh {resultado}')

