"""Basic tests -- run with: pytest test_calculator.py"""

from calculator import add, subtract, divide, average


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    # This test currently FAILS -- that's the point, it exposes the bug.
    # Once fixed, divide(10, 0) should raise a clear, handled error
    # (e.g. ValueError) instead of crashing with ZeroDivisionError.
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)
