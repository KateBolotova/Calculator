from pytest_bdd import given, when, then, scenario, parsers
from calculator import equation_irr
from sympy import SympifyError


@scenario('../equation_irrational.feature', 'Вычисление корней системы уравнений')
def test_system():
    pass


@scenario('../equation_irrational.feature', 'Вычисление корней системы уравнений, когда в одном уравнении y = 0')
def test_system_y0():
    pass


@scenario('../equation_irrational.feature', 'Вычисление корней системы уравнений, когда в одном уравнении x = 0')
def test_system_x0():
    pass


@scenario('../equation_irrational.feature',
          'Вычисление корней системы уравнений, когда в одном уравнении есть буквенный символ')
def test_system_a():
    pass


@scenario('../equation_irrational.feature',
          'Вычисление корней системы уравнений, когда в одном уравнении есть иные символы')
def test_system_error():
    pass


@given(parsers.parse('Первое уравнение {eq_string}'), target_fixture='first_eq')
def first_eq(eq_string):
    equation = eq_string
    return equation


@given(parsers.parse('Второе уравнение {eq_string}'), target_fixture='second_eq')
def second_eq(eq_string):
    equation = eq_string
    return equation


@when('Я пытаюсь найти решение этого уравнения', target_fixture='found_roots')
def solve_eq(first_eq, second_eq):
    eqs = [first_eq, second_eq]
    roots = equation_irr(eqs)
    return roots


@when('Я пытаюсь найти решение этого уравнения и ожидаю ошибку', target_fixture='equation_error')
def solve_eq_error(first_eq, second_eq):
    eqs = [first_eq, second_eq]
    try:
        equation_irr(eqs)
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
