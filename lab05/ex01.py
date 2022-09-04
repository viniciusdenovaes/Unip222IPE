entrada = input('Entre com uma lista de inteiros separados por espaço: ')

# Retira todos os espaços vazios do começo e do final da string
entrada = entrada.strip()

# Retira espaços duplos (se dois números estiveram separados por dois ou mais espaços)
# Enquanto ainda existir dois espaços vazios na string, estes dois espaços serão substituídos por um espaço
while '  ' in entrada:
    entrada = entrada.replace('  ', ' ')

lista_entrada = entrada.split(' ')

inteiros = []

for digito_string in lista_entrada:
    digito_inteiro = int(digito_string)
    inteiros.append(digito_inteiro)

print(f'O tamanho da lista eh {len(inteiros)}')

print('lista: ', inteiros)

