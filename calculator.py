def matrix_det(matrix_count_det):

    # Проверка типов элементов матрицы
    for row in matrix_count_det:
        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError("Матрица должна содержать только числа")

    a = matrix_count_det[0][0]
    b = matrix_count_det[0][1]
    c = matrix_count_det[0][2]
    d = matrix_count_det[1][0]
    e = matrix_count_det[1][1]
    f = matrix_count_det[1][2]
    g = matrix_count_det[2][0]
    h = matrix_count_det[2][1]
    i = matrix_count_det[2][2]

    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

    return det
