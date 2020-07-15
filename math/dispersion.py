import numpy as np

# получение дисперсии значений массива
# в случае многомерного масиива - дисперсии строк


def get_dispersion(x_i):
    i = 0
    if len(x_i.shape) != 1:
        result = np.var(x_i, axis=1)
    else:
        result = np.var(x_i)
    return result
