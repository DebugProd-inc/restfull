import numpy as np
import random
import scipy
import scipy.spatial


confidence_probability = 0.95  # уровень доверительной вероятности
# может задаваться пользователем. По умолчанию значение 0,95

Init_X = None
Init_distance = None
math_expected_Func = None
dispersion_Func = None
geometric_center = None
MU_MAX = None
cov_matrix = None

confidence_probability = 0.95  # уровень доверительной вероятности
# может задаваться пользователем. По умолчанию значение 0,95


# функция возвращает вектор мат. ожиданий параметров
def center(x_i):
    result = np.zeros(len(x_i))
    i = 0
    for row in x_i:
        result[i] += sum(row)/len(x_i)
        i += 1
    return result


# функция возвращает вектор дисперисии параметров
def dispersion(x_i):
    if len(x_i.shape) != 1:
        result = np.var(x_i, axis=1)
    else:
        result = np.var(x_i)
    return result


# функция возвращает вектор расстояний параметров от мат. ожиданий
def mahalanob(x_i, X_C):
    global cov_matrix
    result = np.zeros(
        len(x_i[0])
        )
    invers_cov_matrix = np.linalg.inv(cov_matrix)
    i = 0
    for i in range(0, len(x_i[0])):
        result[i] = scipy.spatial.distance.mahalanobis(
            x_i[:, i], X_C, invers_cov_matrix
            )
        i += 1
    return result


# функция получения квантили от выборки
def getting_quantile(confidence_probability):
    global Init_distance
    return np.quantile(Init_distance, confidence_probability)


# функция уточнения начальных значений
def refinement_of_initial_values(Xj):
    # добавление значений к начальным
    global Init_X
    Init_X = np.concatenate((Init_X, Xj), axis=1)
    Beginning_of_work(Init_X)


# функция проверки текущего тех. состояния
def functional_check(Xj):
    global MU_MAX
    dj = mahalanob(Xj, geometric_center)
    if max(dj) <= MU_MAX:
        # максимальное значение дистанции параметров
        # должно быть не более квантиля доверительной вероятности
        return True
    else:
        return False


def Beginning_of_work(X):
    global Init_X
    global Init_distance
    global math_expected_Func
    global dispersion_Func
    global geometric_center
    global confidence_probability
    global MU_MAX
    global cov_matrix
    Init_X = X  # вектор (матрица) выборки
    cov_matrix = np.cov(Init_X)
    geometric_center = center(X)  # геометрический центр
    Init_distance = mahalanob(Init_X, geometric_center)  # дистанция выборки
    math_expected_Func = center(Init_distance)  # мат. ожидание дистанции
    dispersion_Func = dispersion(Init_distance)  # дисперсия дистанции
    MU_MAX = getting_quantile(confidence_probability)
    # ^^^получение квантили доверительной вероятности^^^


# функция изменения уровня доверительной вероятности
def Change_confidence_probability(new_confidence_probability):
    global confidence_probability
    global MU_MAX
    confidence_probability = new_confidence_probability
    MU_MAX = getting_quantile(confidence_probability)

# print("norm")
