from __future__ import annotations
from typing import Iterable
from numbers import Number
from collections import namedtuple
from itertools import combinations
from sympy.matrices import Matrix


class Vector(tuple):
    def __new__(self, *args: Iterable[Number]) -> Vector:
        return super().__new__(self, args)


class Point(namedtuple('Point', ['x', 'y'])):
    def __new__(self, x: Vector, y: Vector) -> Point:
        return super().__new__(self, x, y)


class Piece(tuple):
    def __new__(self, *args: Iterable[Point]) -> Piece:
        assert len(set([len(arg.y) for arg in args])) == 1
        assert len(set([arg.x for arg in args])) == len(args)
        assert all([len(arg.x)+1 == len(args) for arg in args])
        return super().__new__(self, args)


class PLF(tuple):
    def __new__(self, *args: Iterable[Piece]) -> PLF:
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
            return Vector(*y)

        raise AssertionError
