import math


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
    if x > 18:
        raise ValueError("Вводите числа в диапазоне [1; 18]")
    res = round(fac(x) / math.e)
    return res


# функция вычисления корней квадратного уравнения
def equation_quad(coeffs):
    roots = [0] * 2
    a, b, c = coeffs
    if a == 0:
        raise ZeroDivisionError("Коэффициент переменной в квадрате не равен 0 в квадратичной функции")
    for value in coeffs:
        if not isinstance(value, (int, float)):
            raise ValueError("Квадратичныя функция должна содержать только численные коэффициенты")
    D = b ** 2 - 4 * a * c
    if D > 0:
        roots[0] = (-b + D ** 0.5) / (2 * a)
        roots[1] = (-b - D ** 0.5) / (2 * a)
    elif D == 0:
        del roots[1:]
        roots = -b / (2 * a)
    else:
        del roots[1:]
        roots = None
    return roots


def equation_system(A, b):
    n = len(b)

    matrix_A = A
    matrix_b = b

    for a in matrix_A:
        for b1 in a:
            if not isinstance(b1, (int, float)):
                raise ValueError("Система уравнений должна содержать только численные коэффициенты")

    for i in range(n):
        for j in range(i + 1, n):
            if matrix_A[i][i] == 0:
                return None
            factor = matrix_A[j][i] / matrix_A[i][i]
            for col in range(i, n):
                matrix_A[j][col] -= factor * matrix_A[i][col]
            matrix_b[j] -= factor * matrix_b[i]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix_b[i]
        for j in range(i + 1, n):
            x[i] -= matrix_A[i][j] * x[j]
        if matrix_A[i][i] == 0:
            return None
        x[i] /= matrix_A[i][i]

    return x
