import pytest
from calculator import matrix_det


def test_empty_matrix():
    assert matrix_det([]) == 0


def test_zero_matrix():
    assert matrix_det([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0


@pytest.mark.parametrize('array,expect', [
    ([[1, 1, 1], [2, 2, 2], [1, 1, 1]],
     0),

    ([[1, 2, 3], [1, 2, 4], [1, 2, 5]],
     0),

    ([[1, 2, 3], [2, 4, 6], [6, 6, 6]],
     0),
])
def test_zero_det(array, expect):
    assert matrix_det(array) == expect


@pytest.mark.parametrize('array,expect', [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 10]],
     -3),

    ([[2, 4, 6], [1, 3, 5], [0, 2, 7]],
     4),

    ([[1, 1, 2], [2, 3, 4], [3, 4, 5]],
     -1),
])
def test_ordinary_det(array, expect):
    assert matrix_det(array) == expect

