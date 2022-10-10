
def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado


assert fatorial(0) == 1
assert fatorial(1) == 1
assert fatorial(2) == 2
assert fatorial(3) == 6
assert fatorial(4) == 24
