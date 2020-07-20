import numpy as np
import random
import scipy
import scipy.spatial
import TV_i_MS
import test_values
import functional_check
"""     
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
"""
"""
# функция возвращает вектор мат. ожиданий параметров
def center(x_i):
    result = np.zeros(len(x_i))
    i = 0
    for row in x_i:
        result[i] += sum(row)/len(x_i)
        i += 1
    return result


def dispersion(x_i):
    M_x_i = center(x_i)
    i = 0
    for row in x_i:
        result[i] += sum(row - M_x_i[i])/len(x_i)
        i += 1
    return result
"""

# X_C = center(implementation_values)

"""
# функция возвращает вектор расстояний параметров от мат. ожиданий
def mahalanob(x_i):
    result = np.zeros(
        len(x_i[0])
        )
    cov_matrix = np.cov(implementation_values)
    invers_cov_matrix = np.linalg.inv(cov_matrix)
    i = 0
    for i in range(0, len(x_i[0])):
        result[i] = scipy.spatial.distance.mahalanobis(
            x_i[:, i], X_C, invers_cov_matrix
            )
        i += 1
    return result


# функция получения квантили от выборки
def getting_quantile(dj, confidence_probability):
    return np.quantile(dj, confidence_probability)


confidence_probability = float(input())  # ввод с консоли для проверки

MU_MAX = getting_quantile(mahalanob(implementation_values))

"""
"""
# функция проверки текущего тех. состояния
def functional_check(d_i):
    if max(d_i) <= MU_MAX:
        # максимальное значение дистанции параметров
        # должно быть не более квантиля доверительной вероятности
        return True

    else:
        return False
"""


def update_values(Xj):
    global Init_X
    Init_X = np.concatenate(
        (Init_X, Xj), axis=1
        )
    begin(Init_X)


X_C = get_center.get_center()


def begin(Xi):
    global Init_X
    global X_C
    global distance
    global Veybull
    Init_X = Xi
    X_C = get_center.get_center(Xi)
    distance = mahalanob(Xi)
    Veybull = TV_i_MS.Class_distribution_func(distance)


def check(confidence_level, Xj):
    global Veybull
    global distance
    MU_max = Veybull.get_quantile(confidence_level)
    flag = functional_check.functional_check(distance, mu_max)
    if (flag):
        update_values(Xj)
    return flag
