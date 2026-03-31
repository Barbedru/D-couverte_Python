

from calculator import add, sub, mult

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert sub(10, 4) == 6

def test_multiply():
    assert mult(3, 4) == 12
