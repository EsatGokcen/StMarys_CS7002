import pytest
from week9 import calculator

def test_add():
    expected = 8
    actual = calculator.add(5,3)
    assert actual == expected, "Error - expected 8"