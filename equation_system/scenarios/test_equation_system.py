from pytest_bdd import given, when, then, scenario, parsers
from calculator import equation_system


@scenario('../equation_system.feature', 'Вычисление корней системы уравнений c тремя функциями')
def test_system():
    pass

@given(parsers.parse('Левая часть уравнений {eq_string}'), target_fixture='left_part')
def left_part(eq_string):
    equation_matrix = eq_string
    return equation_matrix


@given(parsers.parse('Правая часть уравнений {eq_string}'), target_fixture='right_part')
def right_part(eq_string):
    equation_matrix = eq_string
    return equation_matrix


@when('Я пытаюсь найти решение этого уравнения', target_fixture='found_roots')
def solve_eq(left_part, right_part):
    roots = equation_system(left_part, right_part)
    return roots

