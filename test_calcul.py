

from simple_code import SimpleCode

calc = SimpleCode()

def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.sub(10, 4) == 6


def test_multiply():
    assert calc.mult(3, 4) == 12
