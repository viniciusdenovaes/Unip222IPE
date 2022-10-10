
def tamanho_palavras(palavras):
    resultado = []
    for p in palavras:
        resultado.append(len(p))
    return resultado


assert tamanho_palavras([]) == []
assert tamanho_palavras(['']) == [0]
assert tamanho_palavras(['f']) == [1]
assert tamanho_palavras(['foo']) == [3]
assert tamanho_palavras(['foo', 'bar']) == [3, 3]
assert tamanho_palavras(['foo', 'bar', 'pal']) == [3, 3, 3]
assert tamanho_palavras(['', 'b', 'pal']) == [0, 1, 3]
