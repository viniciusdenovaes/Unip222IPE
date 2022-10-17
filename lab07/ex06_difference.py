
def diferenca(l1, l2):
    return set(l1).difference(set(l2))


assert diferenca([], []) == set()
assert diferenca([1], []) == {1}
assert diferenca([], [1]) == set()
assert diferenca([1], [1]) == set()
assert diferenca([1], [2]) == {1}
assert diferenca([1, 2], [1, 2]) == set()
assert diferenca([1, 2, 4], [1, 2, 3]) == {4}
