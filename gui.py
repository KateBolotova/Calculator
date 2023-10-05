import tkinter as tk
from tkinter import ttk

import calculator


# Функции для переключения между экранами
def show_matrices_screen():
    hide_all_screens()
    matrices_screen.pack()


def show_matrices_1():
    hide_all_screens()
    matrices_1.pack()


def show_matrices_2():
    hide_all_screens()
    matrices_2.pack()


def show_equations_screen():
    hide_all_screens()
    equations_screen.pack()


def show_equations_1():
    hide_all_screens()
    equations_1.pack()


def show_equations_2():
    hide_all_screens()
    equations_2.pack()


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
    matrices_1.pack_forget()
    matrices_2.pack_forget()
    equations_1.pack_forget()
    equations_2.pack_forget()


# Создаем главное окно
root = tk.Tk()
root.title("Научный калькулятор")
root.geometry('600x600')

# Стиль
style = ttk.Style()
style.configure("My.TButton", font=("Arial", 16), foreground="black", background="lightgray")

# Создаем экраны для каждой функциональности
matrices_screen = tk.Frame(root)
matrices_1 = tk.Frame(root)
matrices_2 = tk.Frame(root)
equations_screen = tk.Frame(root)
equations_1 = tk.Frame(root)
equations_2 = tk.Frame(root)
integration_screen = tk.Frame(root)
main_screen = tk.Frame(root)

# Экран "Матриц"
matrices_label = tk.Label(matrices_screen, text="Экран с матрицами")
matrices_label.pack()
matrices_back_button = ttk.Button(matrices_screen, text="На главный экран", command=show_main_screen,
                                  style="My.TButton")
matrices_back_button.pack()

# Доп Кнопки для экрана с матрицами
matrices_1_button = ttk.Button(matrices_screen, text="Test Driven Development - Сложение двух матриц 3x3",
                               command=show_matrices_1,
                               style="My.TButton")
matrices_1_button.pack()
matrices_2_button = ttk.Button(matrices_screen, text="Behavior Driven Development", command=show_matrices_2,
                               style="My.TButton")
matrices_2_button.pack()

# Сумма матриц 3 на 3
matrices_label = tk.Label(matrices_1, text="Экран со сложением матриц")
matrices_label.pack()
matrices_back_button = ttk.Button(matrices_1, text="На главный экран", command=show_main_screen,
                                  style="My.TButton")
matrices_back_button.pack()

# Экран "Уравнения"
equations_label = tk.Label(equations_screen, text="Экран с уравнениями")
equations_label.pack()
equations_back_button = ttk.Button(equations_screen, text="На главный экран", command=show_main_screen,
                                   style="My.TButton")
equations_back_button.pack()

# Доп Кнопки для экрана с уравнениями
equations_1_button = ttk.Button(equations_screen, text="Функция 1", command=show_equations_1, style="My.TButton")
equations_1_button.pack()
equations_2_button = ttk.Button(equations_screen, text="Функция 2", command=show_equations_2, style="My.TButton")
equations_2_button.pack()

# Экран "Интегрирование"
integration_label = tk.Label(integration_screen, text="Экран с интегрированием")
integration_label.pack()
integration_back_button = ttk.Button(integration_screen, text="На главный экран", command=show_main_screen,
                                     style="My.TButton")
integration_back_button.pack()

# Главный экран
main_label = tk.Label(main_screen, text="Главный экран")
main_label.pack()
matrices_button = ttk.Button(main_screen, text="Матрицы", command=show_matrices_screen, style="My.TButton")
equations_button = ttk.Button(main_screen, text="Уравнения", command=show_equations_screen, style="My.TButton")
integration_button = ttk.Button(main_screen, text="Интегрирование", command=show_integration_screen, style="My.TButton")

matrices_button.pack()
equations_button.pack()
integration_button.pack()

# Запускаем главное окно
show_main_screen()  # Показываем начальный экран при запуске приложения
root.mainloop()
