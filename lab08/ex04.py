

def get_valor(dicionario: dict, chave):
    if chave in dicionario.keys():
        return dicionario[chave]
    return None


assert get_valor({}, 0) is None
assert get_valor({0: 'zero'}, 0) == 'zero'
assert get_valor({0: 'zero', 1: 'um'}, 1) == 'um'
assert get_valor({0: 'zero', 1: 'um'}, 2) is None
