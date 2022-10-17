
def lista_to_conjunto(lista):
    return set(lista)


assert lista_to_conjunto([]) == set()
assert lista_to_conjunto([1]) == {1}
assert lista_to_conjunto([1, 2]) == {1, 2}
assert lista_to_conjunto([1, 2, 1]) == {1, 2}
