import update_values
import numpy as np

# проверка функциональности ВС
# сравнение расстояния от геометрического центра с максимальным
# если расстояние меньше или равно допустимому, то оно
# записывается в доспустимые значения


def functional_check(distance, mu_max):
    if max(distance) <= mu_max:
        return True
    else:
        return False


# пример добавления элементов в массив distance
"""distance = np.array([0, 0, 1])
distance = np.matrix(distance)
distance = np.transpose(distance)"""
