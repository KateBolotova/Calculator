import pytest
from calculator import equation_quad

#S1 Тесты с обычными вводными данными и результатами
@pytest.mark.parametrize('coeff,roots', [
    ([1, -3, 2], [2, 1]),
    ([1, -15, 14], [14, 1]),
    ([1, -7, 12], [4, 3])
])
def test_simple_quad(coeff, roots):
    assert equation_quad(coeff) == roots
#S2 Тест с отрицательными корнями
@pytest.mark.parametrize('coeff,roots', [
    ([1, 2, -8], [2, -4]),
    ([1, 3, -4], [1, -4]),
    ([1, 2, 1], [-1, -1]),
    ([2, 4, 2], [-1, -1])
])
def test_simple_quad(coeff, roots):
    assert equation_quad(coeff) == roots

#S2 Тесты на неполные квадраты, ноль, отсутствие корней

@pytest.mark.parametrize('coeff,roots', [
    ([0, 3, -6], [2, -2]),
    ([2, 0, -8], [2, -2]),
    ([2, -8, 0], [4, 0]),
    ([0, 0, 0], None)
])
def test_uncompleted_quad(coeff, roots):
    assert equation_quad(coeff) == roots

def test_no_roots():
    assert equation_quad([1, 2, 8]) == None

def test_D_equal_to_zero():
    assert equation_quad([1, -4, 4]) == [2, 2]

