entrada = input('Entre com uma lista de inteiros separados por espaço: ')

entrada = entrada.strip()
while '  ' in entrada:
    entrada = entrada.replace('  ', ' ')
lista_entrada = entrada.split(' ')

inteiros = []
for digito_string in lista_entrada:
    digito_inteiro = int(digito_string)
    inteiros.append(digito_inteiro)

print(f'O primeiro  elemento eh {inteiros[0]} e o ultimo eh{inteiros[-1]}')

