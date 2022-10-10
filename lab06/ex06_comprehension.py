
def primeira_letra(palavras):
    return [p[0] for p in palavras]


assert primeira_letra([]) == []
assert primeira_letra(['foo']) == ['f']
assert primeira_letra(['foo', 'bar']) == ['f', 'b']
assert primeira_letra(['foo', 'bar', 'pal']) == ['f', 'b', 'p']
