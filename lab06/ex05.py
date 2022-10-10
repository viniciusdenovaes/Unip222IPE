
def inverte(lista):
    resultado = []
    for i in range(len(lista)):
        resultado.append(lista[-i-1])
    return resultado


assert inverte([]) == []
assert inverte([1]) == [1]
assert inverte([1, 2, 3]) == [3, 2, 1]
assert inverte(['foo', 'bar', 'palavra', 'fao']) == ['fao', 'palavra', 'bar', 'foo']
