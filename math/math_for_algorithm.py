import numpy as np
import random
import scipy
import scipy.spatial


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
    i = 0
    if len(x_i.shape) != 1:
        result = np.var(x_i, axis=1)
    else:
        result = np.var(x_i)
    return result


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


# класс выборочной функции распределения
class Selective_distribution_func:
    # функция получения квантили от выборки
    def getting_quantile(self, confidence_probability):
        return np.quantile(self.dj, confidence_probability)

    def __init__(self, dj, math_expected, dispersion):  # конструктор
        self.dj = dj
        self.math_expected = center(dj)
        self.dispersion = dispersion(dj)


# Класс начальных значений.
class initial_values:
    def __init__(self, X):
        self.Init_X = X  # вектор (матрица) выборки
        # объект класса выборочной функции распределения
        self.distribution_function = Selective_distribution_function(
            mahalanob(X)
            )
        self.geometric_center = center(X)  # геометрический центр

    def refinement_of_initial_values(self, Xj):
        # добавление значений к начальным
        self.Init_X = np.concatenate((self.Init_X, Xj), axis=1)
        # объект класса выборочной функции распределения
        self.distribution_function = Selective_distribution_func(
            mahalanob(self.Init_X)
            )
        self.geometric_center = center(self.Init_X)  # геометрический центр


class technical_condition_estimation_algorithm:
    def __init__(self, Init_X, confidence_probability):
        self.confidence_probability = confidence_probability
        self.init_values = initial_values(Init_X)
        # получение квантили доверительной вероятности
        self.MU_MAX = self.init_values.distribution_function.getting_quantile(
            self.confidence_probability
            )

    # функция проверки текущего тех. состояния
    def functional_check(d_i):
        if max(d_i) <= self.MU_MAX:
            # максимальное значение дистанции параметров
            # должно быть не более квантиля доверительной вероятности
            return True
        else:
            return False

    def current_value_processing(self, Xj):
        dj = mahalanob(Xj)
        return self.functional_check(dj)
