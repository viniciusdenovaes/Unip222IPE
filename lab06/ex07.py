
def primeira_letra(palavras):
    resultado = []
    for p in palavras:
        resultado.append(p[-1])
    return resultado


assert primeira_letra([]) == []
assert primeira_letra(['foo']) == ['o']
assert primeira_letra(['foo', 'bar']) == ['o', 'r']
assert primeira_letra(['foo', 'bar', 'pal']) == ['o', 'r', 'l']
