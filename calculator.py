import math
from sympy import symbols, Eq, solve, sympify


def matrix_det(matrix):
    # Проверка типов элементов матрицы
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError("Матрица должна содержать только числа")

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = a * e * i + b * f * g + c * d * h - c * e * g - b * d * i - a * f * h
    return det


def add_matrices(m1, m2):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            if not isinstance(m1[i][j], (int, float)) or not isinstance(m2[i][j], (int, float)):
                raise ValueError("Матрицы должны содержать только числа")
            result[i][j] = m1[i][j] + m2[i][j]
    return result


def fac(x):
    if not isinstance(x, int) or x < 0:
        raise ValueError("Вводите только целые неотрицательные числа")
    if x == 0 or x == 1:
        return 1
    return x * fac(x - 1)


def subfac(x):
    if not isinstance(x, int) or x <= 0:
        raise ValueError("Вводите только целые положительные числа")
    res = round(fac(x)/math.e)
    return res

  
#функция вычисления корней квадратного уравнения
def equation_quad(coeffs):
    roots = [0]*2
    a, b, c = coeffs
    if a == 0:
        raise ZeroDivisionError("Коэффициент переменной в квадрате не равен 0 в квадратичной функции")
    for value in coeffs:
        if not isinstance(value, (int, float)):
            raise ValueError("Квадратичныя функция должна содержать только численные коэффициенты")
    D = b**2 -4*a*c
    if D>0:
        roots[0] = (-b + D**0.5) / (2*a)
        roots[1] = (-b - D**0.5) / (2*a)
    elif D == 0:
        del roots[1:]
        roots = -b / (2*a)
    else:
        del roots[1:]
        roots = None
    return roots


def equation_system():
    return