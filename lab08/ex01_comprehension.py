

def make_palavra_tamanho(palavras):
    return {p: len(p) for p in palavras}


assert make_palavra_tamanho([]) == {}
assert make_palavra_tamanho(['banana']) == {'banana': 6}
assert make_palavra_tamanho(['banana', 'maca']) == {'banana': 6, 'maca': 4}
assert make_palavra_tamanho(['banana', 'maca', 'pera']) == {'banana': 6, 'maca': 4, 'pera': 4}
