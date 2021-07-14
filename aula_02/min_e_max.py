from typing import Iterable, Tuple, Iterator
from numbers import Number
from math import inf


def _min_max_recursiva(iterador: Iterator, valor_min: Number, valor_max: Number):
    try:
        elemento = next(iterador)
    except StopIteration:
        return valor_min, valor_max

    else:
        if elemento < valor_min:
            valor_min = elemento
        if elemento > valor_max:
            valor_max = elemento
        return _min_max_recursiva(iterador, valor_min, valor_max)



def min_max(iteravel: Iterable) -> Tuple [Number, Number]:
    """
    >>> min_max([])
    Traceback (most recent call last):
        ...
    ValueError: Não exixte mínimo e maximo de iterável sem valor

    >>> min_max([1])
    (1, 1)



    :return:
    """
    iterador = iter(iteravel)
    valor_minimo, valor_maximo = _min_max_recursiva(iterador, inf, -inf)
    if valor_minimo is inf:
        raise ValueError('Não exixte mínimo e maximo de iterável sem valor')
    return valor_minimo, valor_maximo