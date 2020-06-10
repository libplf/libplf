from libplf import plf
from libplf import piece
from libplf import point
from libplf import vector


def test_libplf_case_0001():
    try:
        plf()
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_0002():
    f = plf(
        piece(
            point(
                vector(0),
                vector(0),
            ),
            point(
                vector(1),
                vector(1),
            ),
        )
    )
    assert f(0.5) == vector(0.5)


def test_libplf_case_0003():
    f = plf(
        piece(
            point(
                vector(0),
                vector(0),
            ),
            point(
                vector(1),
                vector(1),
            ),
        ),
        piece(
            point(
                vector(1),
                vector(1),
            ),
            point(
                vector(2),
                vector(3),
            ),
        )
    )
    assert f(0.5) == vector(0.5)
    assert f(1) == vector(1)
    assert f(1.5) == vector(2)
    assert f(2) == vector(3)


def test_libplf_case_0004():
    try:
        plf(
            piece(
                point(
                    vector(0),
                    vector(0),
                ),
                point(
                    vector(1),
                    vector(1),
                ),
            ),
            piece(
                point(
                    vector(1),
                    vector(1),
                ),
                point(
                    vector(0),
                    vector(0),
                ),
            )
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_0005():
    try:
        plf(
            piece(
                point(
                    vector(0),
                    vector(0),
                ),
                point(
                    vector(2),
                    vector(1),
                ),
            ),
            piece(
                point(
                    vector(1),
                    vector(1),
                ),
                point(
                    vector(3),
                    vector(0),
                ),
            )
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_0006():
    try:
        plf(
            piece(
                point(
                    vector(0),
                    vector(0),
                ),
                point(
                    vector(2),
                    vector(1),
                ),
            ),
            piece(
                point(
                    vector(0),
                    vector(1),
                ),
                point(
                    vector(3),
                    vector(0),
                ),
            )
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_0007():
    try:
        plf(
            piece(
                point(
                    vector(0),
                    vector(0),
                ),
                point(
                    vector(4),
                    vector(1),
                ),
            ),
            piece(
                point(
                    vector(2),
                    vector(1),
                ),
                point(
                    vector(3),
                    vector(0),
                ),
            )
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_0008():
    try:
        plf(
            piece(
                point(
                    vector(0, 0),
                    vector(0),
                ),
                point(
                    vector(0, 1),
                    vector(1),
                ),
                point(
                    vector(1, 0),
                    vector(2),
                ),
            ),
            piece(
                point(
                    vector(0, 0),
                    vector(0),
                ),
                point(
                    vector(0, 2),
                    vector(1),
                ),
                point(
                    vector(2, 0),
                    vector(2),
                ),
            ),
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_0009():
    try:
        plf(
            piece(
                point(
                    vector(2, 2),
                    vector(0),
                ),
                point(
                    vector(0, 1),
                    vector(1),
                ),
                point(
                    vector(1, 0),
                    vector(2),
                ),
            ),
            piece(
                point(
                    vector(0, 0),
                    vector(0),
                ),
                point(
                    vector(0, 2),
                    vector(1),
                ),
                point(
                    vector(2, 0),
                    vector(2),
                ),
            ),
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_000A():
    try:
        plf(
            piece(
                point(
                    vector(2, 2),
                    vector(0),
                ),
                point(
                    vector(-1, 1),
                    vector(1),
                ),
                point(
                    vector(1, -1),
                    vector(2),
                ),
            ),
            piece(
                point(
                    vector(0, 0),
                    vector(0),
                ),
                point(
                    vector(0, 2),
                    vector(1),
                ),
                point(
                    vector(2, 0),
                    vector(2),
                ),
            ),
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_000B():
    try:
        plf(
            piece(
                point(
                    vector(1, 1),
                    vector(0),
                ),
                point(
                    vector(1, 2),
                    vector(1),
                ),
                point(
                    vector(2, 1),
                    vector(2),
                ),
            ),
            piece(
                point(
                    vector(0, 0),
                    vector(0),
                ),
                point(
                    vector(0, 2),
                    vector(1),
                ),
                point(
                    vector(2, 0),
                    vector(2),
                ),
            ),
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_000C():
    try:
        plf(
            piece(
                point(
                    vector(1, 1),
                    vector(0),
                ),
                point(
                    vector(1, 2),
                    vector(1),
                ),
                point(
                    vector(0, 2),
                    vector(2),
                ),
            ),
            piece(
                point(
                    vector(0, 0),
                    vector(0),
                ),
                point(
                    vector(0, 2),
                    vector(1),
                ),
                point(
                    vector(2, 0),
                    vector(2),
                ),
            ),
        )
    except:
        pass
    else:
        raise RuntimeError


def test_libplf_case_000D():
    f = plf(
        piece(
            point(
                vector(0, 0),
                vector(0),
            ),
            point(
                vector(0, 1),
                vector(1),
            ),
            point(
                vector(1, 0),
                vector(2),
            ),
        ),
        piece(
            point(
                vector(2, 2),
                vector(0),
            ),
            point(
                vector(3, 2),
                vector(1),
            ),
            point(
                vector(2, 3),
                vector(2),
            ),
        ),
    )

    assert f(2, 3) == vector(2)


def test_libplf_case_000E():
    try:
        plf(
            piece(
                point(
                    vector(0, 0),
                    vector(0),
                ),
                point(
                    vector(0, 1),
                    vector(1),
                ),
                point(
                    vector(0, 2),
                    vector(2),
                ),
            ),
        )
    except:
        pass
    else:
        raise RuntimeError
