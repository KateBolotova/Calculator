Feature: Сложение двух матриц 3x3
  Я как пользователь
  Хочу сложить две матрицы 3x3
  Чтобы получить результат

  Scenario: Сложение двух матриц 3x3
    Given Первая матрица [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    And Вторая матрица [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    When Я складываю их
    Then Результат должен быть [[10, 10, 10], [10, 10, 10], [10, 10, 10]]

  Scenario: Сложение двух матриц 3x3, где одна нулевая
    Given Первая матрица [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    And Вторая матрица [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    When Я складываю их
    Then Результат должен быть [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  Scenario: Сложение двух матриц 3x3, где есть отрицательные элементы
    Given Первая матрица [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    And Вторая матрица [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    When Я складываю их
    Then Результат должен быть [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

  Scenario: Сложение двух матриц 3x3, где есть буквы
    Given Первая матрица [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    And Вторая матрица [['a', 'b', 'c'], [6, 5, 4], [3, 2, 1]]
    When Я складываю их и ожидаю ошибку
    Then Исключение должно быть ValueError
