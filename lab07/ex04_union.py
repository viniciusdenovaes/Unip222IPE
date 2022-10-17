
def uniao(l1, l2):
    return set(l1).union(set(l2))


assert uniao([], []) == set()
assert uniao([1], []) == {1}
assert uniao([], [1]) == {1}
assert uniao([1], [1]) == {1}
assert uniao([1], [2]) == {1, 2}
assert uniao([1, 2], [1, 2]) == {1, 2}
assert uniao([1, 2, 4], [1, 2, 3]) == {1, 2, 3, 4}
