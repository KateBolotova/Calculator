import pytest
from calculator import fac

def test_digit():
    with pytest.raises(ValueError):
        fac('a')

def test_empty():
    with pytest.raises(TypeError):
        fac()

@pytest.mark.parametrize('num, expect', [(0, 1), (1, 1)])

def test_0_and_1(num, expect):
    assert fac(num) == expect