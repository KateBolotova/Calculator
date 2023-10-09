import pytest
from calculator import equation_quad

#предполагаемая функция equation_quad, вычисляющая корни квадратного уравнения
@pytest.mark.parametrize('coeff,roots', [
    ([1, -3, 2], [2, 1]),
    ([1, -15, 14], [14, 1]),
    ([1, -7, 12], [3, 4])
])
def test_simple_quad(coeff, roots):
    assert equation_quad(coeff) == roots
