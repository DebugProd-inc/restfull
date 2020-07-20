import numpy as np
import scipy
import scipy.spatial
import math
# from test_values import confidence_probability

# получение из выборки расстояний Махаланобиса при штатном
# функционировании квантили заднного уровня
S = 0  # степень полинома я хз как её реально найти, так что от балды


def get_quantile(dj, confidence_probability):
    return np.quantile(dj, confidence_probability)


# МНК оценка коэфициентов
def parameter_estimation(X, Y):
    X_ = X.transpose()
    result = np.dot(X_, X)
    result = np.linalg.inv(result)
    result = np.dot(result, X_)
    result = np.dot(result, Y)
    return result


def get_func(dj):
    dj.sort()
    f = []
    for i in range(0, len(dj)):
        p = i/len(dj)
        f.append(p)
    return f


def get_X_Matrix(dj):
    global S
    S = len(dj)
    New_d = []
    for i in range(0, len(dj)):
        New_d.append([])
        for j in range(S + 1, 0):
            New_d[i].append(dj[i]**j)
    return New_d


class Class_distribution_func:
    def __init__(self, dj):
        self.d = dj.sort()
        fun = lambda x: (-(math.log(1-x)))  # ему не нравится лямбда
        # но мне пофиг, потому что мне нравится)))))
        B_ = map(fun, get_func(dj))
        self.parameters = parameter_estimation(
            get_X_Matrix(dj),
            np.transpose(B_)
            )

    def B_Veybull(self, x):
        return np.polyval(self.parameters, x)

    def get_value(self, x):
        return 1 - (math.e**(-self.B_Veybull(x)))
    
    def get_quantile(self, alfa):
        B_ = (-(math.log(1-alfa)))
        param = np.copy(self.parameters)
        param[len(B_)-1] -= B_
        roots = np.roots(param)
        roots = filter(lambda x: (x >= 0) and
        (isinstance(x, float)), roots)
        return min(roots)  # выбор корня подвергается критике
        # я хз пока как делать правильно, так что пока так
