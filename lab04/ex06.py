numero = int(input('Entre com um numero inteiro: '))

somatorio = 0

while numero > 0:

    # pegando o digito mais a direita do numero
    digito = numero % 10
    # somando digito no acumulador
    somatorio += digito
    print(f'Somando o digito {digito}. Somatorio = {somatorio}')

    # retirando o digito mais a direita do numero
    numero = numero // 10

print(f'A soma dos digitos sera {somatorio}')
