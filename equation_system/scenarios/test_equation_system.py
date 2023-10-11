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

@then(parsers.parse('Результат должен быть {roots_str}'))
def check_result(found_roots, roots_str):
    roots = eval(roots_str)
    assert found_roots == roots

