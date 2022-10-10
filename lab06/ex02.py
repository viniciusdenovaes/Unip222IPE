
def somatorio(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


assert somatorio([]) == 0
assert somatorio([1]) == 1
assert somatorio([1, 2]) == 3
assert somatorio([1, 2, 3]) == 6
assert somatorio([1, -1, 1, -1]) == 0
assert somatorio([-10, -1, -10, -1]) == -22

