
def tamanho_palavras(palavras):
    return [len(p) for p in palavras]


assert tamanho_palavras([]) == []
assert tamanho_palavras(['']) == [0]
assert tamanho_palavras(['f']) == [1]
assert tamanho_palavras(['foo']) == [3]
assert tamanho_palavras(['foo', 'bar']) == [3, 3]
assert tamanho_palavras(['foo', 'bar', 'pal']) == [3, 3, 3]
assert tamanho_palavras(['', 'b', 'pal']) == [0, 1, 3]
