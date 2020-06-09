from __future__ import annotations
from typing import Iterable
from numbers import Number
from sympy.matrices import Matrix
from ..vector import T as vector
from ..piece import T as piece


class T(tuple):
    def __new__(self, *args: Iterable[piece]) -> T:
        # TODO: validation
        return super().__new__(self, args)

    def __call__(self, *args: Iterable[Number]) -> Iterable[Number]:
        # TODO: validation

        for piece in self:
            r = Matrix([arg for arg in args] + [1])
            X = [point.x for point in piece]
            S = [point for point in zip(*X)]
            R = Matrix(S + [[1]*len(piece)])
            l = R.inv() * r
            if max(l) > 1:
                continue
            if min(l) < 0:
                continue
            Y = [point.y for point in piece]
            T = Matrix([point for point in zip(*Y)])
            y = T * l
            return vector(*y)

        raise AssertionError
