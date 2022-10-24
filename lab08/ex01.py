

def make_palavra_tamanho(palavras):
    palavra_tamanho = {}
    for p in palavras:
        palavra_tamanho[p] = len(p)
    return palavra_tamanho


assert make_palavra_tamanho([]) == {}
assert make_palavra_tamanho(['banana']) == {'banana': 6}
assert make_palavra_tamanho(['banana', 'maca']) == {'banana': 6, 'maca': 4}
assert make_palavra_tamanho(['banana', 'maca', 'pera']) == {'banana': 6, 'maca': 4, 'pera': 4}
