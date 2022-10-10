def is_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def quantidade_primos(numeros):
    quantidade = 0
    for n in numeros:
        if is_primo(n):
            quantidade += 1
    return quantidade


assert quantidade_primos([]) == 0
assert quantidade_primos([2]) == 1
assert quantidade_primos([3]) == 1
assert quantidade_primos([4]) == 0
assert quantidade_primos([4, 5]) == 1
assert quantidade_primos([3, 5]) == 2
assert quantidade_primos([3, 3]) == 2
assert quantidade_primos([3, 3, 3]) == 3
assert quantidade_primos([4, 8, 16]) == 0
assert quantidade_primos([3, 5, 7]) == 3
