Feature: Вычисление субфакториала
  Я как пользователь
  Хочу вычислить субфакториал
  Чтобы получить результат

  Scenario: Вычисление субфакториала отрицательного числа
    Given Значение -1
    When Я пытаюсь вычислить его субфакториал
    Then Должно быть вызвано исключение ValueError
