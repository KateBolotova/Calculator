from pytest_bdd import given, when, then, scenario, parsers
from calculator import add_matrices


@scenario('../matrix_addition.feature', 'Сложение двух матриц 3x3')
def test_addition():
    pass


@scenario('../matrix_addition.feature', 'Сложение двух матриц 3x3, где одна нулевая')
def test_addition_zero_matrix():
    pass


@scenario('../matrix_addition.feature', 'Сложение двух матриц 3x3, где есть отрицательные элементы')
def test_addition_negative_matrix():
    pass


@scenario('../matrix_addition.feature', 'Сложение двух матриц 3x3, где есть буквы')
def test_addition_with_letters():
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


@when('Я складываю их и ожидаю ошибку', target_fixture='addition_error')
def step_when_add_matrices_with_error(first_matrix, second_matrix):
    try:
        add_matrices(first_matrix, second_matrix)
    except Exception as e:
        return e


@then(parsers.parse('Исключение должно быть {error_type_string}'))
def check_result(addition_error, error_type_string):
    error_type = eval(error_type_string)
    assert isinstance(addition_error, error_type)


@then(parsers.parse('Результат должен быть {matrix_string}'))
def check_result(added_matrices, matrix_string):
    matrix = eval(matrix_string)
    assert added_matrices == matrix
