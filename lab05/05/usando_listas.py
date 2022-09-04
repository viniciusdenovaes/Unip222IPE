lista1 = input('Entre com a primeira lista de inteiros separados por espaço: ')
lista2 = input('Entre com a segunda lista de inteiros separados por espaço: ')

lista1 = lista1.strip()
lista2 = lista2.strip()

while '  ' in lista1:
    lista1 = lista1.replace('  ', ' ')

while '  ' in lista2:
    lista2 = lista2.replace('  ', ' ')

lista1 = lista1.split(' ')
lista2 = lista2.split(' ')

numeros1 = []
for digito_string in lista1:
    digito_inteiro = int(digito_string)
    numeros1.append(digito_inteiro)

numeros2 = []
for digito_string in lista2:
    digito_inteiro = int(digito_string)
    numeros2.append(digito_inteiro)

resultado = []
for numero in numeros1:
    if numero not in resultado:
        if numero in numeros2:
            resultado.append(numero)

print('conjunto: ', resultado)

