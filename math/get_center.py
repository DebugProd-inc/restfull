import numpy as np


# получение координат геометрического центра
def get_center(x_i):
    result = np.zeros(len(x_i))
    i = 0
    for row in x_i:
        result[i] += sum(row)/len(x_i)
        i += 1
    return result
