
def fatorial(n):
    if n == 0:
        return 1
    return n*fatorial(n-1)


assert fatorial(0) == 1
assert fatorial(1) == 1
assert fatorial(2) == 2
assert fatorial(3) == 6
assert fatorial(4) == 24
