Feature: Вычисление корней системы уравнений с помощью Гаусса
  Я как пользователь
  Хочу найти корни системы уравнений
  Чтобы получить результат

  Scenario: Вычисление корней системы уравнений c тремя функциями
    Given Левая часть уравнений [[1, -1, 2], [2, 1, -1], [3, 3, 3]]
    And Правая часть уравнений [6, 3, 15]
    When Я пытаюсь найти решение этого уравнения
    Then Результат должен быть [3.0, 2.0, 1.0]

  Scenario: Вычисление корней системы уравнений c тремя функциями
    Given Левая часть уравнений [[2, 1, -1], [1, 1, 1], [3, 2, 3]]
    And Правая часть уравнений [8, 6, 14]
    When Я пытаюсь найти решение этого уравнения
    Then Результат должен быть [2.0, 4.0, 0.0]
