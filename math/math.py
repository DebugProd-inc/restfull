import numpy as np
import random
import scipy
import scipy.spatial

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
IMPLEMENTATION_VALUES = np.row_stack((x1, x2, x3))


def center(x_i):
    result = np.zeros(len(x_i))
    i = 0
    for row in x_i:
        result[i] += sum(row)/len(x_i)
        i += 1
    return result


X_C = center(IMPLEMENTATION_VALUES)


def dispersion(x_i):
    i = 0
    if len(x_i.shape) != 1:
        result = np.var(x_i, axis=1)
    else:
        result = np.var(x_i)
    return result


def mahalanob(x_i):
    result = np.zeros(
        len(x_i[0])
        )
    cov_matrix = np.cov(IMPLEMENTATION_VALUES)
    invers_cov_matrix = np.linalg.inv(cov_matrix)
    i = 0
    for i in range(0, len(x_i[0])):
        result[i] = scipy.spatial.distance.mahalanobis(
            x_i[:, i], X_C, invers_cov_matrix
            )
        i += 1
    return result


def getting_quantile(dj):
    confidence_probability = float(input())
    return np.quantile(dj, confidence_probability)


MU_MAX = getting_quantile(mahalanob(IMPLEMENTATION_VALUES))


def functional_check(distance):
    if distance <= MU_MAX:
        return True
    else:
        return False
