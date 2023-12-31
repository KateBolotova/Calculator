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


def show_fact_screen():
    hide_all_screens()
    fact_screen.pack()


def show_fact_1():
    hide_all_screens()
    fact_1.pack()


def show_fact_2():
    hide_all_screens()
    fact_2.pack()


def show_main_screen():
    hide_all_screens()
    main_screen.pack()


# Функция для скрытия всех экранов
def hide_all_screens():
    matrices_screen.pack_forget()
    equations_screen.pack_forget()
    fact_screen.pack_forget()
    main_screen.pack_forget()
    matrix_sum.pack_forget()
    matrix_det.pack_forget()
    equations_1.pack_forget()
    equations_2.pack_forget()
    fact_1.pack_forget()
    fact_2.pack_forget()


def count_det():
    matrix_count_det = []
    try:
        for i in range(3):
            matrix_count_det.append([])
            for j in range(3):
                value = float(matrix_det_entries[i][j].get())
                matrix_count_det[-1].append(value)
        res = calculator.matrix_det(matrix_count_det)
        matrix_res.config(text=str(res))
    except:
        matrix_res.config(text='Ошибка!')


def count_sum():
    matrix_count_sum_1 = []
    matrix_count_sum_2 = []
    try:
        for i in range(3):
            matrix_count_sum_1.append([])
            matrix_count_sum_2.append([])
            for j in range(3):
                value_1 = float(matrix1_entries[i][j].get())
                value_2 = float(matrix2_entries[i][j].get())
                matrix_count_sum_1[-1].append(value_1)
                matrix_count_sum_2[-1].append(value_2)
        res = calculator.add_matrices(matrix_count_sum_1, matrix_count_sum_2)
        str_matrix = ''
        for i in range(3):
            for j in range(3):
                str_matrix += f'{res[i][j]:8.2f}'
            str_matrix += '\n'
        matrix_sum_res.config(text=str_matrix)
    except:
        matrix_sum_res.config(text='Ошибка!')


def find_quad_roots():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        coeffs = [a_val, b_val, c_val]
        str_roots = str(calculator.equation_quad(coeffs))
        equation_roots.config(text=str_roots)
    except ValueError:
        equation_roots.config(text="Проверьте, что ввели численные значения")
    except ZeroDivisionError:
        equation_roots.config(text="Уравнение не имеет решений")

def find_system_roots():
    try:
        A = []
        b = []
        for i in range(3):
            equation = []
            for j in range(4):
                equation.append(float(matrix_entries[i][j].get()))
            A.append(equation[:-1])
            b.append(equation[-1])

        solutions = calculator.equation_system(A, b)
        if solutions is None:
            equation_roots_sys.config(text="Решений нет")
        else:
            equation_roots_sys.config(text=f"Решение: {solutions}")
    except:
        equation_roots_sys.config(text="Проверьте, что ввели численные значения")


def count_fac():
    try:
        res = calculator.fac(int(x_fac.get()))
        fac_res.config(text=f'{res}')
    except ValueError:
        fac_res.config(text='Вводите только целые неотрицательные числа')
    except TypeError:
        fac_res.config(text='Введите число!')

        
def count_subfac():
    try:
        res = calculator.subfac(int(x_subfac.get()))
        subfac_res.config(text=f'{res}')
    except:
        subfac_res.config(text='Вводите только целые положительные числа в диапазоне [1; 18]')


# Создаем главное окно
root = tk.Tk()
root.title("Научный калькулятор")
root.geometry('800x300')

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
fact_screen = tk.Frame(root)
fact_1 = tk.Frame(root)
fact_2 = tk.Frame(root)
main_screen = tk.Frame(root)

# Экран "Матриц"
matrices_label = tk.Label(matrices_screen, text="Экран с матрицами")
matrices_label.pack()
matrices_back_button = ttk.Button(matrices_screen, text="На главный экран", command=show_main_screen,
                                  style="My.TButton")
matrices_back_button.pack()

# Доп Кнопки для экрана с матрицами
matrices_2_button = ttk.Button(matrices_screen, text="TDD - Нахождение определителя для "
                                                     "матрицы 3x3", command=show_matrix_det,
                               style="My.TButton")
matrices_2_button.pack()
matrices_1_button = ttk.Button(matrices_screen, text="BDD - Сложение двух матриц 3x3",
                               command=show_matrix_sum,
                               style="My.TButton")
matrices_1_button.pack()

# Сумма матриц 3 на 3 - поле ввода
matrices_label = tk.Label(matrix_sum, text="Экран со сложением матриц")
matrices_label.grid(row=0, column=0, columnspan=3)

matrices_back_button = ttk.Button(matrix_sum, text="На главный экран", command=show_main_screen, style="My.TButton")
matrices_back_button.grid(row=1, column=0, columnspan=3)

matrix1_label = tk.Label(matrix_sum, text="Матрица 1:")
matrix1_label.grid(row=2, column=0)

matrix1_entries = []
for i in range(3):
    matrix1_entries.append([])
    for j in range(3):
        entry = tk.Entry(matrix_sum, width=5)
        entry.grid(row=i + 3, column=j)
        matrix1_entries[-1].append(entry)

matrix_sign = tk.Label(matrix_sum, text="+")
matrix_sign.grid(row=6, column=0, columnspan=3)
matrix2_label = tk.Label(matrix_sum, text="Матрица 2:")
matrix2_label.grid(row=7, column=0)

matrix2_entries = []
for i in range(3):
    matrix2_entries.append([])
    for j in range(3):
        entry = tk.Entry(matrix_sum, width=5)
        entry.grid(row=i + 8, column=j)
        matrix2_entries[-1].append(entry)

matrix2_label = tk.Label(matrix_sum, text="")
matrix2_label.grid(row=11, column=0)
perform_operation_button = ttk.Button(matrix_sum, text="Выполнить операцию", command=count_sum, style="My.TButton")
perform_operation_button.grid(row=12, column=0, columnspan=3)
matrix_sum_res = tk.Label(matrix_sum, text="")
matrix_sum_res.grid(row=13, column=0, columnspan=3)

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

tk.Label(matrix_det, text="").grid(row=11, column=0)
perform_operation_button = ttk.Button(matrix_det, text="Выполнить операцию", command=count_det, style="My.TButton")
perform_operation_button.grid(row=12, column=0, columnspan=3)
matrix_res = tk.Label(matrix_det, text="")
matrix_res.grid(row=13, column=0, columnspan=3)

# Экран "Уравнения"
equations_label = tk.Label(equations_screen, text="Экран с уравнениями")
equations_label.pack()
equations_back_button = ttk.Button(equations_screen, text="На главный экран", command=show_main_screen,
                                   style="My.TButton")
equations_back_button.pack()

# Доп Кнопки для экрана с уравнениями
equations_1_button = ttk.Button(equations_screen, text="TDD - Корни квадратичной функции", command=show_equations_1, style="My.TButton")
equations_1_button.pack()
equations_2_button = ttk.Button(equations_screen, text="BDD - Решения системы уравнений", command=show_equations_2, style="My.TButton")
equations_2_button.pack()

#Экран уравнения квадратичные - поля ввода
equations_label = tk.Label(equations_1, text="Экран с решением квадратичных функций")
equations_label.grid(row=0, column=0, columnspan=5)

equations_back_button = ttk.Button(equations_1, text="На главный экран", command=show_main_screen, style="My.TButton")
equations_back_button.grid(row=1, column=0, columnspan=5)

equation_quad_name = tk.Label(equations_1, text="Квадратичное уравнение:")
equation_quad_name.grid(row=3, column=0, columnspan=5)

a = ttk.Entry(equations_1, width=3)
a.grid(row=4,column=0)
a_lab = ttk.Label(equations_1, text="x**2 + ").grid(row=4,column=1)

b = ttk.Entry(equations_1, width=3)
b.grid(row=4,column=2)
b_lab = ttk.Label(equations_1, text="x + ").grid(row=4, column=3)

c = ttk.Entry(equations_1, width=3)
c.grid(row=4, column=4)
c_lab = ttk.Label(equations_1, text=" = 0").grid(row=4, column=5)

perform_operation_button = ttk.Button(equations_1, text="Выполнить операцию", command=find_quad_roots, style="My.TButton")
perform_operation_button.grid(row=5, column=0, columnspan=5)
equation_roots = tk.Label(equations_1, text="")
equation_roots.grid(row=13, column=0, columnspan=5)

#Экран система уравнений - поля ввода
equations_label = tk.Label(equations_2, text="Экран с решением системы уравнений")
equations_label.grid(row=0, column=0, columnspan=7)

equations_back_button = ttk.Button(equations_2, text="На главный экран", command=show_main_screen, style="My.TButton")
equations_back_button.grid(row=1, column=0, columnspan=7)

equation_quad_name = tk.Label(equations_2, text="Система уравнений (вписать данные в порядке коэффициентов a, b, c, d и к чему уравнение приравнено:")
equation_quad_name.grid(row=3, column=0, columnspan=7)

matrix_entries = []
for i in range(3):
    equation_label = tk.Label(equations_2, text=f"Уравнение {i + 1}:")
    equation_label.grid(row=i+4, column=0)

    equation_entry = []
    for j in range(4):
        entry = tk.Entry(equations_2)
        entry.grid(row=i+4, column=j+4)
        equation_label = ttk.Label(equations_2).grid(row=i + 4, column=j+5)
        equation_entry.append(entry)

    matrix_entries.append(equation_entry)

perform_operation_button = ttk.Button(equations_2, text="Выполнить операцию", command=find_system_roots, style="My.TButton")
perform_operation_button.grid(row=7, column=0, columnspan=7)
equation_roots_sys = tk.Label(equations_2, text="")
equation_roots_sys.grid(row=8, column=0, columnspan=7)

# Экран "(Суб)факториал"
fact_label = tk.Label(fact_screen, text="Экран с вычислением (суб)факториала")
fact_label.pack()
fact_back_button = ttk.Button(fact_screen, text="На главный экран", command=show_main_screen,
                              style="My.TButton")
fact_back_button.pack()

# Доп Кнопки для экрана с (суб)факториалом
fact_1_button = ttk.Button(fact_screen, text="TDD Факториал", command=show_fact_1, style="My.TButton")
fact_1_button.pack()
fact_2_button = ttk.Button(fact_screen, text="BDD Субфакториал", command=show_fact_2, style="My.TButton")
fact_2_button.pack()

# Экран Факториала
fac_label = tk.Label(fact_1, text="Экран факториала")
fac_back_button = ttk.Button(fact_1, text="На главный экран", command=show_main_screen, style="My.TButton")
fac_label.pack()
fac_back_button.pack()

fac_l = tk.Label(fact_1, text="Введите целое неотрицательное число")
x_fac = tk.Entry(fact_1, width=30)
fac_l.pack()
x_fac.pack()

fac_button = ttk.Button(fact_1, text="Рассчитать!", command=count_fac, style="My.TButton")
fac_button.pack()
fac_res = tk.Label(fact_1, text="")
fac_res.pack()

# Экран Субфакториала
subfac_label = tk.Label(fact_2, text="Экран субфакториала")
subfac_back_button = ttk.Button(fact_2, text="На главный экран", command=show_main_screen, style="My.TButton")
subfac_label.pack()
subfac_back_button.pack()

subfac_l = tk.Label(fact_2, text="Введите целое положительное число < 19")
x_subfac = tk.Entry(fact_2, width=30)
subfac_l.pack()
x_subfac.pack()

subfac_button = ttk.Button(fact_2, text="Рассчитать!", command=count_subfac, style="My.TButton")
subfac_button.pack()
subfac_res = tk.Label(fact_2, text="")
subfac_res.pack()

# Главный экран
main_label = tk.Label(main_screen, text="Главный экран")
main_label.pack()
matrices_button = ttk.Button(main_screen, text="Матрицы", command=show_matrices_screen, style="My.TButton")
equations_button = ttk.Button(main_screen, text="Уравнения", command=show_equations_screen, style="My.TButton")
fact_button = ttk.Button(main_screen, text="(Суб)факториал", command=show_fact_screen, style="My.TButton")

matrices_button.pack()
equations_button.pack()
fact_button.pack()

# Запускаем главное окно
show_main_screen()  # Показываем начальный экран при запуске приложения
root.mainloop()
