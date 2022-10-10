
def primeira_letra(palavras):
    resultado = []
    for p in palavras:
        resultado.append(p[0])
    return resultado


assert primeira_letra([]) == []
assert primeira_letra(['foo']) == ['f']
assert primeira_letra(['foo', 'bar']) == ['f', 'b']
assert primeira_letra(['foo', 'bar', 'pal']) == ['f', 'b', 'p']
