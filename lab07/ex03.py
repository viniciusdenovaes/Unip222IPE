
def conjunto_pares(lista):
    conjunto_total = set(lista)
    conjunto_pares = set()
    for e in conjunto_total:
        if e%2 == 0:
            conjunto_pares.add(e)

    return conjunto_pares


assert conjunto_pares([]) == set()
assert conjunto_pares([1]) == set()
assert conjunto_pares([2]) == {2}
assert conjunto_pares([1, 2]) == {2}
assert conjunto_pares([1, 2, 2]) == {2}

