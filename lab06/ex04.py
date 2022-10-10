# Fibonacci sequence:
# a_1 = 1,
# a_2 = 1,
# a_n = a_{n-1} + a_{n-2}

def fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    sequencia = [1, 1]
    for _ in range(3, n+1):
        proximo_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_numero)
    return sequencia[-1]


assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(8) == 21
assert fibonacci(9) == 34

