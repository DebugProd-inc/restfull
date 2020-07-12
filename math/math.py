# from __future__ import division
import numpy as np
import random
import scipy
import scipy.spatial

# test values of implementation
x1 = np.array([random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4)])
x2 = np.array([random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4)])
x3 = np.array([random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4), random.gauss(2, 4)])

# переменная для хранения массивов начальных значений
implementation_values = np.row_stack((x1, x2, x3))


def center(n, x_i):
    result = np.zeros(n)
    i = 0
    for row in x_i:
        result[i]+=sum(row)/n
        i += 1
    return result


x_c = center(len(implementation_values), implementation_values)


def mahalanob(x_i):
    result = np.zeros(len(x_i[0]))
    cov_matrix = np.cov(implementation_values)
    invers_cov_matrix = np.linalg.inv(cov_matrix)
    i = 0
    for i in range(0, len(x_i[0])):
        result[i] = scipy.spatial.distance.mahalanobis(x_i[:, i], x_c, invers_cov_matrix)
        i=i+1
    return result


mahalanob_test = mahalanob(implementation_values)

print("M_D = ", mahalanob_test)
