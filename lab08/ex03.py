

def existe_valor(dicionario: dict, chave):
    return chave in dicionario.values()


assert existe_valor({}, 0) is False
assert existe_valor({0: 'zero'}, 'zero') is True
assert existe_valor({0: 'zero', 1: 'um'}, 'um') is True
assert existe_valor({0: 'zero', 1: 'um'}, 2) is False
