from pytest_bdd import given, when, then, scenario, parsers
from calculator import subfac


@scenario('scenarios/subfactorial.feature', 'Вычисление субфакториала отрицательного числа')
def test_negative():
    pass

@scenario('scenarios/subfactorial.feature', 'Вычисление субфакториала крайнего числа')
def test_0():
    pass

@scenario('scenarios/subfactorial.feature', 'Вычисление субфакториала символа')
def test_digit():
    pass

@scenario('scenarios/subfactorial.feature', 'Вычисление субфакториала числа')
def test_subfac():
    pass

@given(parsers.parse('Значение {x}'), target_fixture='value')
def value(x):
    v = eval(x)
    return v

@when('Я вычисляю его субфакториал', target_fixture='subfac')
def subfac_error(value):
    res = subfac(value)
    return res

@when('Я пытаюсь вычислить его субфакториал', target_fixture='e')
def subfac_error(value):
    try:
        subfac(value)
    except Exception as e:
        return e

@then(parsers.parse('Должно быть вызвано исключение {error_type}'))
def check_result(e, error_type):
    error = eval(error_type)
    assert isinstance(e, error)

@then(parsers.parse('Результат должен быть {result}'))
def check_result(subfac, result):
    res = eval(result)
    assert subfac == res
