from pytest_bdd import given, when, then, scenario, parsers
from calculator import add_matrices


@scenario('../matrix_addition.feature', 'Сложение двух матриц 3x3')
def test_addition():
    pass


@given(parsers.parse('Первая матрица {matrix_string}'), target_fixture='first_matrix')
def first_matrix(matrix_string):
    matrix = eval(matrix_string)
    return matrix


@given(parsers.parse('Вторая матрица {matrix_string}'), target_fixture='second_matrix')
def second_matrix(matrix_string):
    matrix = eval(matrix_string)
    return matrix


@when('Я складываю их', target_fixture='added_matrices')
def add_matrices_step(first_matrix, second_matrix):
    result_matrix = add_matrices(first_matrix, second_matrix)
    return result_matrix


@then(parsers.parse('Результат должен быть {matrix_string}'))
def check_result(added_matrices, matrix_string):
    matrix = eval(matrix_string)
    assert added_matrices == matrix
