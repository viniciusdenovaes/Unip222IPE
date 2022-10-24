

def conta_elementos(lista):
    resultado = {}
    for e in lista:
        if e not in resultado.keys():
            resultado[e] = 0
        resultado[e] += 1
    return resultado


assert conta_elementos([]) == {}
assert conta_elementos(['banana']) == {'banana': 1}
assert conta_elementos(['banana', 'maca']) == {'banana': 1, 'maca': 1}
assert conta_elementos(['banana', 'maca', 'banana']) == {'banana': 2, 'maca': 1}

