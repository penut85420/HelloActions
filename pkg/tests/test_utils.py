from ..utils import plus, minus, multi, intdiv, moddiv

def test_calc():
    assert plus(3, 4) == 7
    assert minus(5, 6) == -1
    assert multi(7, 8) == 56
    assert intdiv(7, 3) == 2
    assert moddiv(5, 2) == 1
