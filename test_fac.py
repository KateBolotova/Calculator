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


@pytest.mark.parametrize('num, expect', [(5, 120), (2, 2), (7, 5040)])
def test_fac(num, expect):
    assert fac(num) == expect


def test_negative():
    with pytest.raises(ValueError):
        fac(-2)
