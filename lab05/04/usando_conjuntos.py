entrada = input('Entre com uma lista de inteiros separados por espaço: ')

entrada = entrada.strip()
while '  ' in entrada:
    entrada = entrada.replace('  ', ' ')
lista_entrada = entrada.split(' ')

inteiros = set()
for digito_string in lista_entrada:
    digito_inteiro = int(digito_string)
    inteiros.add(digito_inteiro)

print('conjunto: ', inteiros)

