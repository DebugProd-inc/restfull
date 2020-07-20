import numpy as np
# from test_values import confidence_probability

# получение из выборки расстояний Махаланобиса при штатном
# функционировании квантили заднного уровня
s = 0  # степень полинома


def get_quantile(dj, confidence_probability):
    return np.quantile(dj, confidence_probability)


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
    i = 0
    for a in dj:
        i += 1
        p = i/len(dj)
        f.append(p)
    return f


def get_X_Matrix(dj):
    