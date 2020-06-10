from __future__ import annotations
from typing import Iterable
from numbers import Number
from sympy.matrices import Matrix
from ..vector import T as vector
from ..piece import T as piece
from random import choice
from itertools import combinations


class T(tuple):
    def __new__(self, *args: Iterable[piece]) -> T:
        assert len(args) > 0
        for arg in args:
            assert isinstance(arg, piece)
        assert len(set([len(arg) for arg in args])) == 1
        assert len(set([len(choice(arg).y) for arg in args])) == 1

        for a, b in combinations(args, 2):
            Ra, Rb = a.R(), b.R()
            K = Ra.inv() * Rb
            print(Ra)
            print(Rb)
            print(K)
            M = [(min(K.row(i)), max(K.row(i))) for i in range(K.rows)]
            if all([p > 1 or q < 0 for p, q in M]):
                continue
            if any([p < 1 and q > 0 for p, q in M]):
                raise AssertionError

            for point in a:
                if point in b:
                    continue
                l = b.barycentric_coordinate(*point.x)
                if max(l) > 1:
                    continue
                if min(l) < 0:
                    continue
                raise AssertionError

            for point in b:
                if point in a:
                    continue
                l = a.barycentric_coordinate(*point.x)
                if max(l) > 1:
                    continue
                if min(l) < 0:
                    continue
                raise AssertionError

        return super().__new__(self, args)

    def __call__(self, *args: Iterable[Number]) -> Iterable[Number]:
        assert len(args) + 1 == len(choice(self))

        for piece in self:
            l = piece.barycentric_coordinate(*args)
            if max(l) > 1:
                continue
            if min(l) < 0:
                continue
            Y = [point.y for point in piece]
            T = Matrix([point for point in zip(*Y)])
            y = T * l
            return vector(*y)

        raise AssertionError
