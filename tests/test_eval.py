from pytest import raises
from libplf import plf
from libplf import piece
from libplf import point
from libplf import vector


class Test:
    def test(self):
        f = plf(*self.args())
        for x, y in self.rets():
            assert f(*x) == y

    def args(self):
        return [
            piece(
                point(vector(0), vector(0)),
                point(vector(1), vector(1)),
            )
        ]

    def rets(self):
        return []


class Test_1_1(Test):
    def args(self):
        return [
            piece(
                point(vector(ax), vector(ay)),
                point(vector(bx), vector(by)),
            )
            for (ax, ay), (bx, by) in self.defs()
        ]

    def defs(self):
        return [
            [(0, 0), (1, 1)],
        ]


class Test_1_2(Test):
    def args(self):
        return [
            piece(
                point(vector(ax), vector(ay, az)),
                point(vector(bx), vector(by, bz)),
            )
            for (ax, ay, az), (bx, by, bz) in self.defs()
        ]

    def defs(self):
        return [
            [(0, 0, 0), (1, 1, 1)],
        ]


class Test_2_1(Test):
    def args(self):
        return [
            piece(
                point(vector(ax, ay), vector(az)),
                point(vector(bx, by), vector(bz)),
                point(vector(cx, cy), vector(cz)),
            )
            for
            (ax, ay, az),
            (bx, by, bz),
            (cx, cy, cz),
            in self.defs()
        ]

    def defs(self):
        return [
            [
                (0, 0, 0),
                (1, 0, 1),
                (0, 1, 2),
            ],
        ]
