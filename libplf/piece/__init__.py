from __future__ import annotations
from typing import Iterable
from ..point import T as point


class T(tuple):
    def __new__(self, *args: Iterable[point]) -> T:
        assert len(set([len(arg.y) for arg in args])) == 1
        assert len(set([arg.x for arg in args])) == len(args)
        assert all([len(arg.x)+1 == len(args) for arg in args])
        return super().__new__(self, args)
