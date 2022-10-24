from typing import List, Dict


def make_lista_compras(produtos: List[str], precos: Dict[str, float]):
    resultado = {}
    for p in produtos:
        if p not in resultado.keys():
            resultado[p] = 0
        resultado[p] += precos[p]

    return resultado


assert make_lista_compras([], {}) == {}
assert make_lista_compras([], {'banana': 2}) == {}
assert make_lista_compras([], {'banana': 2, 'maca': 4, 'pera': 2, 'uva': 6}) == {}
assert make_lista_compras(['banana'], {'banana': 2, 'maca': 4, 'pera': 2, 'uva': 6}) == {'banana': 2}
assert make_lista_compras(['banana', 'maca'], {'banana': 2, 'maca': 4, 'pera': 2, 'uva': 6}) == {'banana': 2, 'maca': 4}
assert make_lista_compras(['banana', 'maca', 'pera', 'banana'], {'banana': 2, 'maca': 4, 'pera': 2, 'uva': 6}) == {'banana': 4, 'maca': 4, 'pera': 2}



