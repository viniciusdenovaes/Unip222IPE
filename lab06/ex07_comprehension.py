
def primeira_letra(palavras):
    return [p[-1] for p in palavras]


assert primeira_letra([]) == []
assert primeira_letra(['foo']) == ['o']
assert primeira_letra(['foo', 'bar']) == ['o', 'r']
assert primeira_letra(['foo', 'bar', 'pal']) == ['o', 'r', 'l']
