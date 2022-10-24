from typing import Dict


def make_preco_produto(precos: Dict[str, float]):
    resultado: Dict[float, set] = {}
    for produto, preco in precos.items():
        if preco not in resultado.keys():
            resultado[preco] = set()
        resultado[preco].add(produto)
    return resultado


assert make_preco_produto({}) == {}
assert make_preco_produto({'banana': 2}) == {2: {'banana'}}
assert make_preco_produto({'banana': 2, 'maca': 3}) == {2: {'banana'}, 3: {'maca'}}
assert make_preco_produto({'banana': 2, 'maca': 3, 'pera': 2}) == {2: {'banana', 'pera'}, 3: {'maca'}}

