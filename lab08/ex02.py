

def existe_chave(dicionario: dict, chave):
    return chave in dicionario.keys()


assert existe_chave({}, 0) is False
assert existe_chave({0: 'zero'}, 0) is True
assert existe_chave({0: 'zero', 1: 'um'}, 1) is True
assert existe_chave({0: 'zero', 1: 'um'}, 2) is False
