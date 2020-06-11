from pytest import raises
from libplf import plf
from libplf import piece
from libplf import point
from libplf import vector


class Test:
    def test(self):
        with raises(AssertionError):
            plf(*self.args())

    def args(self):
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
        return []


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
        return []


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
        return []


class Test_1_1_Dup(Test_1_1):
    def defs(self):
        return [
            [(0, 0), (1, 1)],
            [(1, 1), (0, 0)],
        ]


class Test_1_1_Overlap(Test_1_1):
    def defs(self):
        return [
            [(0, 0), (2, 2)],
            [(1, 1), (3, 3)],
        ]


class Test_1_1_Longer(Test_1_1):
    def defs(self):
        return [
            [(0, 0), (2, 2)],
            [(0, 0), (3, 3)],
        ]


class Test_1_1_Contain(Test_1_1):
    def defs(self):
        return [
            [(1, 1), (2, 2)],
            [(0, 0), (3, 3)],
        ]


class Test_1_1_Step(Test_1_1):
    def defs(self):
        return [
            [(1, 1), (2, 2)],
            [(2, 3), (3, 3)],
        ]


class Test_1_2_Dup(Test_1_2):
    def defs(self):
        return [
            [(0, 0, 0), (1, 1, 1)],
            [(1, 1, 1), (0, 0, 0)],
        ]


class Test_1_2_Overlap(Test_1_2):
    def defs(self):
        return [
            [(0, 0, 0), (2, 2, 2)],
            [(1, 1, 1), (3, 3, 3)],
        ]


class Test_1_2_Longer(Test_1_2):
    def defs(self):
        return [
            [(0, 0, 0), (2, 2, 2)],
            [(0, 0, 0), (3, 3, 3)],
        ]


class Test_1_2_Contain(Test_1_2):
    def defs(self):
        return [
            [(1, 1, 1), (2, 2, 2)],
            [(0, 0, 0), (3, 3, 3)],
        ]


class Test_1_2_Step(Test_1_2):
    def defs(self):
        return [
            [(1, 1, 1), (2, 2, 2)],
            [(2, 3, 3), (3, 3, 3)],
        ]


class Test_2_1_Dup(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
        ]


class Test_2_1_Contain(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(-1, -1, 0), (2, 0, 1), (0, 2, 2)],
        ]


class Test_2_1_DualLonger(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(0, 0, 0), (2, 0, 1), (0, 2, 2)],
        ]


class Test_2_1_SingleLonger(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(0, 0, 0), (1, 0, 1), (0, 2, 2)],
        ]


class Test_2_1_ContainEdge(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(0, 0, 0), (1, 0, 1), (1, 1, 2)],
        ]


class Test_2_1_OverlapEdge(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (2, 0, 1), (0, 1, 2)],
            [(0, 0, 0), (1, 0, 1), (1, 1, 2)],
        ]


class Test_2_1_Overlap(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 8, 2)],
            [(-1, 1, 0), (8, 0, 1), (1, 1, 2)],
        ]


class Test_2_1_EdgeStep(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(0, 0, 0), (1, 0, 2), (0, -1, 2)],
        ]


class Test_2_1_EdgeOverlap(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(0, 0, 0), (2, 0, 2), (0, -1, 2)],
        ]


class Test_2_1_PointStep(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (1, 0, 1), (0, 1, 2)],
            [(0, 0, 1), (-1, 0, 2), (0, -1, 2)],
        ]


class Test_2_1_PointOnEdge(Test_2_1):
    def defs(self):
        return [
            [(0, 0, 0), (2, 0, 2), (0, 1, 2)],
            [(1, 0, 1), (-1, -1, 2), (0, -1, 2)],
        ]
