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
    if not isinstance(x, int):
        raise ValueError("Вводите только числа")
    if x == 0 or x == 1:
        return 1
    return x * fac(x - 1)


#функция вычисления корней квадратного уравнения
def equation_quad(coeffs):
    return