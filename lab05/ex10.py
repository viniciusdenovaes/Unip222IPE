import math

entrada = input('Entre com uma lista de números separados por espaço: ')

entrada = entrada.strip()
while '  ' in entrada:
    entrada = entrada.replace('  ', ' ')
lista_entrada = entrada.split(' ')

numeros = []
for digito_string in lista_entrada:
    digito_n = float(digito_string)
    numeros.append(digito_n)

maior = -math.inf
for n in numeros:
    if maior < n:
        maior = n

print(f'O maior numero sera {maior}')

