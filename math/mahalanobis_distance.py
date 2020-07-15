import numpy as np
import scipy
import scipy.spatial
from get_center import get_center
from test_values import IMPLEMENTATION_VALUES

# вычисление расстояний Махаланобиса
# от геометрического центра до текущих координат


def mahalanob(x_i):
    result = np.zeros(
        len(x_i[0])
        )
    cov_matrix = np.cov(IMPLEMENTATION_VALUES)
    invers_cov_matrix = np.linalg.inv(cov_matrix)
    i = 0
    for i in range(0, len(x_i[0])):
        result[i] = scipy.spatial.distance.mahalanobis(
            x_i[:, i], get_center(IMPLEMENTATION_VALUES), invers_cov_matrix
            )
        i += 1
    return result
