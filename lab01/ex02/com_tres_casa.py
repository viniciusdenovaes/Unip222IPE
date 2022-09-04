import math

raio = input('Entre com o raio de um circulo: ')
raio = float(raio)

pi = math.pi

area = pi*(raio**2)

print(f'Area de um circulo de raio {raio} eh: {area:.3f}')
