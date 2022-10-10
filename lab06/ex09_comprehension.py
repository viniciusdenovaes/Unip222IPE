def pares_unicos(lista):
    return list({e for e in lista if e % 2 == 0})


assert set(pares_unicos([])) == set([])
assert set(pares_unicos([1])) == set([])
assert set(pares_unicos([1, 3])) == set([])
assert set(pares_unicos([2])) == {2}
assert set(pares_unicos([2, 2])) == {2}
assert set(pares_unicos([2, 2, 4, 4])) == {2, 4}
assert set(pares_unicos([2, 2, 4, 4, 3, 3])) == {2, 4}
