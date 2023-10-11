from pytest_bdd import given, when, then, scenario, parsers
from calculator import equation_system


@scenario('../equation_system.feature', 'Вычисление корней системы уравнений c тремя функциями')
def test_system():
    pass

@scenario('../equation_system.feature', 'Вычисление корней системы уравнений c тремя функциями (2)')
def test_system2():
    pass

@scenario('../equation_system.feature', 'Вычисление корней системы уравнений c двумя функциями')
def test_system_2eq():
    pass

@scenario('../equation_system.feature', 'Вычисление корней системы уравнений c одной функцией')
def test_system_1eq():
    pass

@scenario('../equation_system.feature','Вычисление корней системы уравнений, когда в одном уравнении есть буквенный символ')
def test_system_a():
    pass

@scenario('../equation_system.feature','Вычисление корней системы уравнений без решения')
def test_system_no_solution():
    pass

@scenario('../equation_system.feature','Вычисление корней системы уравнений с множеством решений')
def test_system_many_solutions():
    pass

@given(parsers.parse('Левая часть уравнений {eq_string}'), target_fixture='left_part')
def left_part(eq_string):
    equation_matrix = eval(eq_string)
    return equation_matrix


@given(parsers.parse('Правая часть уравнений {eq_string}'), target_fixture='right_part')
def right_part(eq_string):
    equation_matrix = eval(eq_string)
    return equation_matrix


@when('Я пытаюсь найти решение этого уравнения', target_fixture='found_roots')
def solve_eq(left_part, right_part):
    roots = equation_system(left_part, right_part)
    return roots

@when('Я пытаюсь найти решение этого уравнения и ожидаю ошибку', target_fixture='equation_error')
def solve_eq_error(left_part, right_part):
    try:
        equation_system(left_part, right_part)
    except Exception as e:
        return e


@then(parsers.parse('Исключение должно быть {error_type_string}'))
def check_result(equation_error, error_type_string):
    error_type = eval(error_type_string)
    assert isinstance(equation_error, error_type)

@then(parsers.parse('Результат должен быть {roots_str}'))
def check_result(found_roots, roots_str):
    roots = eval(roots_str)
    assert found_roots == roots

