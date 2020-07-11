import numpy as np
import scipy
import scipy.spatial

# test values of implementation
x1 = np.array([0.5, 0.3, 0.5, 0.8])
x2 = np.array([0.1, 0.3, 0.5, 0.3])
x3 = np.array([0.3, 0.1, 0.1, 0.1])

implementation_values = np.row_stack((x1, x2, x3))


def center(n, x_i):
    result = np.zeros(n)
    i = 0
    for row in x_i:
        result[i]+=sum(row)/n
        i += 1
    return result


x_c = center(len(implementation_values), implementation_values)

print("X_c = ", x_c)

