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

conjunto1 = set()
for digito_string in lista1:
    digito_inteiro = int(digito_string)
    conjunto1.add(digito_inteiro)

conjunto2 = set()
for digito_string in lista2:
    digito_inteiro = int(digito_string)
    conjunto2.add(digito_inteiro)

resultado = conjunto1 | conjunto2

print('conjunto: ', resultado)

