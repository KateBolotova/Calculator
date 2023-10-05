import tkinter as tk
import calculator


# Функции для переключения между экранами
def show_matrices_screen():
    hide_all_screens()
    matrices_screen.pack()


def show_equations_screen():
    hide_all_screens()
    equations_screen.pack()


def show_integration_screen():
    hide_all_screens()
    integration_screen.pack()


def show_main_screen():
    hide_all_screens()
    main_screen.pack()


# Функция для скрытия всех экранов
def hide_all_screens():
    matrices_screen.pack_forget()
    equations_screen.pack_forget()
    integration_screen.pack_forget()
    main_screen.pack_forget()


# Создаем главное окно
root = tk.Tk()
root.title("Научный калькулятор")

# Создаем экраны для каждой функциональности
matrices_screen = tk.Frame(root)
equations_screen = tk.Frame(root)
integration_screen = tk.Frame(root)
main_screen = tk.Frame(root)

# Экран "Матриц"
matrices_label = tk.Label(matrices_screen, text="Экран с матрицами")
matrices_label.pack()
matrices_back_button = tk.Button(matrices_screen, text="На главный экран", command=show_main_screen)
matrices_back_button.pack()

# Экран "Уравнения"
equations_label = tk.Label(equations_screen, text="Экран с уравнениями")
equations_label.pack()
equations_back_button = tk.Button(equations_screen, text="На главный экран", command=show_main_screen)
equations_back_button.pack()

# Экран "Интегрирование"
integration_label = tk.Label(integration_screen, text="Экран с интегрированием")
integration_label.pack()
integration_back_button = tk.Button(integration_screen, text="На главный экран", command=show_main_screen)
integration_back_button.pack()

# Главный экран
main_label = tk.Label(main_screen, text="Главный экран")
main_label.pack()
matrices_button = tk.Button(main_screen, text="Матрицы", command=show_matrices_screen)
equations_button = tk.Button(main_screen, text="Уравнения", command=show_equations_screen)
integration_button = tk.Button(main_screen, text="Интегрирование", command=show_integration_screen)

matrices_button.pack()
equations_button.pack()
integration_button.pack()

# Запускаем главное окно
show_main_screen()  # Показываем начальный экран при запуске приложения
root.mainloop()
