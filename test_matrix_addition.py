import pytest
from calculator import add_matrices


@pytest.mark.parametrize("first_matrix, second_matrix, expected_result", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
     [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
     [[10, 10, 10], [10, 10, 10], [10, 10, 10]])
])
def test_matrix_addition(first_matrix, second_matrix, expected_result):
    result = add_matrices(first_matrix, second_matrix)
    assert result == expected_result
