
def intersecao(l1, l2):
    return set(l1).intersection(set(l2))


assert intersecao([], []) == set()
assert intersecao([1], []) == set()
assert intersecao([], [1]) == set()
assert intersecao([1], [1]) == {1}
assert intersecao([1], [2]) == set()
assert intersecao([1, 2], [1, 2]) == {1, 2}
assert intersecao([1, 2, 4], [1, 2, 3]) == {1, 2}
