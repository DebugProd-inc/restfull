import numpy as np
import scipy
import scipy.spatial
from get_center import get_center


# вычисление расстояний Махаланобиса
# от геометрического центра до текущих координат
def mahalanob(x_i, x_c, cov_matrix):
    result = np.zeros(
        len(x_i[0])
        )
    invers_cov_matrix = np.linalg.inv(cov_matrix)
    i = 0
    for i in range(0, len(x_i[0])):
        result[i] = scipy.spatial.distance.mahalanobis(
            x_i[:, i], x_c, invers_cov_matrix
            )
        i += 1
    return result
