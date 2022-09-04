entrada = input('Entre com uma lista de inteiros separados por espaço: ')
numero = int(input('Entre com um numero inteiro: '))

entrada = entrada.strip()
while '  ' in entrada:
    entrada = entrada.replace('  ', ' ')
lista_entrada = entrada.split(' ')

inteiros = []
for digito_string in lista_entrada:
    digito_inteiro = int(digito_string)
    inteiros.append(digito_inteiro)

contagem = 0
for n in inteiros:
    if n == numero:
        contagem += 1

print(f'O elemento {numero} aparece em {inteiros}; {contagem} vezes')

