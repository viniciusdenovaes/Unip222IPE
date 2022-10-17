
def somatorio_numeros_unicos(lista):
    conjunto = set(lista)
    soma = 0
    for e in conjunto:
        soma += e

    return soma


assert somatorio_numeros_unicos([]) == 0
assert somatorio_numeros_unicos([1]) == 1
assert somatorio_numeros_unicos([1, 1]) == 1
assert somatorio_numeros_unicos([1, 1, 2]) == 3


