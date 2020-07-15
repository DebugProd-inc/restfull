from math_for_algorithm import *
# test values of implementation
x1 = np.array([
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4)
    ])
x2 = np.array([
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4)
    ])
x3 = np.array([
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4),
    random.gauss(2, 4)
    ])


# переменная для хранения массивов начальных значений
implementation_values = np.row_stack((x1, x2, x3))


# геометрический центр эталонного множества
X_C = center(implementation_values)


confidence_probability = float(input())  # ввод с консоли для проверки


math_for_algorithm.Beginning_of_work(implementation_values)
