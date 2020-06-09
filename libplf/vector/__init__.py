from __future__ import annotations
from typing import Iterable
from numbers import Number


class T(tuple):
    def __new__(self, *args: Iterable[Number]) -> T:
        return super().__new__(self, args)
