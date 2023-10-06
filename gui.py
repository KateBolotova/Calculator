import tkinter as tk
from tkinter import ttk

import calculator


# Функции для переключения между экранами
def show_matrices_screen():
    hide_all_screens()
    matrices_screen.pack()


def show_matrix_sum():
    hide_all_screens()
    matrix_sum.pack()


def show_matrix_det():
    hide_all_screens()
    matrix_det.pack()


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
    matrix_sum.pack_forget()
    matrix_det.pack_forget()
    equations_1.pack_forget()
    equations_2.pack_forget()


def count_det():
    matrix_count_det = []
    for i in range(3):
        matrix_count_det.append([])
        for j in range(3):
            value = float(matrix_det_entries[i][j].get())
            matrix_count_det[-1].append(value)
    print(*matrix_count_det, sep='\n')


# Создаем главное окно
root = tk.Tk()
root.title("Научный калькулятор")
root.geometry('600x600')

# Стиль
style = ttk.Style()
style.configure("My.TButton", font=("Arial", 16), foreground="black", background="lightgray")

# Создаем экраны для каждой функциональности
matrices_screen = tk.Frame(root)
matrix_sum = tk.Frame(root)
matrix_det = tk.Frame(root)
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
matrices_1_button = ttk.Button(matrices_screen, text="TDD - Сложение двух матриц 3x3",
                               command=show_matrix_sum,
                               style="My.TButton")
matrices_1_button.pack()
matrices_2_button = ttk.Button(matrices_screen, text="BDD - Нахождение определителя для "
                                                     "матрицы 3x3", command=show_matrix_det,
                               style="My.TButton")
matrices_2_button.pack()

# Сумма матриц 3 на 3 - поле ввода
matrices_label = tk.Label(matrix_sum, text="Экран со сложением матриц")
matrices_label.grid(row=0, column=0, columnspan=3)

matrices_back_button = ttk.Button(matrix_sum, text="На главный экран", command=show_main_screen, style="My.TButton")
matrices_back_button.grid(row=1, column=0, columnspan=3)

matrix1_label = tk.Label(matrix_sum, text="Матрица 1:")
matrix1_label.grid(row=2, column=0)

matrix1_entries = []
for i in range(3):
    for j in range(3):
        entry = tk.Entry(matrix_sum, width=5)
        entry.grid(row=i + 3, column=j)
        matrix1_entries.append(entry)

matrix_sign = tk.Label(matrix_sum, text="+")
matrix_sign.grid(row=6, column=0, columnspan=3)
matrix2_label = tk.Label(matrix_sum, text="Матрица 2:")
matrix2_label.grid(row=7, column=0)

matrix2_entries = []
for i in range(3):
    for j in range(3):
        entry = tk.Entry(matrix_sum, width=5)
        entry.grid(row=i + 8, column=j)
        matrix2_entries.append(entry)

matrix2_label = tk.Label(matrix_sum, text="")
matrix2_label.grid(row=11, column=0)
perform_operation_button = ttk.Button(matrix_sum, text="Выполнить операцию", style="My.TButton")
perform_operation_button.grid(row=12, column=0, columnspan=3)

# Определитель матрицы 3 на 3 - поле ввода
matrices_label = tk.Label(matrix_det, text="Экран с подсчетом определителя для матрицы 3x3")
matrices_label.grid(row=0, column=0, columnspan=3)

matrices_back_button = ttk.Button(matrix_det, text="На главный экран", command=show_main_screen, style="My.TButton")
matrices_back_button.grid(row=1, column=0, columnspan=3)

matrix_det_label = tk.Label(matrix_det, text="Матрица")
matrix_det_label.grid(row=2, column=0, columnspan=3)

matrix_det_entries = []
for i in range(3):
    matrix_det_entries.append([])
    for j in range(3):
        entry = tk.Entry(matrix_det, width=5)
        entry.grid(row=i + 3, column=j)
        matrix_det_entries[-1].append(entry)

matrix_det_label = tk.Label(matrix_det, text="")
matrix_det_label.grid(row=11, column=0)
perform_operation_button = ttk.Button(matrix_det, text="Выполнить операцию", command=count_det, style="My.TButton")
perform_operation_button.grid(row=12, column=0, columnspan=3)

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
