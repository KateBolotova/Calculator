def matrix_det(matrix_count_det):
    # Проверка типов элементов матрицы
    for row in matrix_count_det:
        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError("Матрица должна содержать только числа")

    if not matrix_count_det:  # Если матрица пустая, возвращаем определитель равный нулю
        return 0

    a, b, c = matrix_count_det[0]
    d, e, f = matrix_count_det[1]
    g, h, i = matrix_count_det[2]

    det = a * e * i + b * f * g + c * d * h - c * e * g - b * d * i - a * f * h
    return det
