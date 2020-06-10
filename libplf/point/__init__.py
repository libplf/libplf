from __future__ import annotations
from ..vector import T as vector
from collections import namedtuple


class T(namedtuple('Point', ['x', 'y'])):
    def __new__(self, x: vector, y: vector) -> T:
        assert isinstance(x, vector)
        assert isinstance(y, vector)
        return super().__new__(self, x, y)
