import math

raio = input('Entre com o raio da esfera: ')
raio = float(raio)

pi = math.pi

area = (4/3)*pi*(raio**3)

print(f'O volume da esfera de {raio} eh: {area}')
