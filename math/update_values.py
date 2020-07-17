import numpy as np
from test_values import implementation_values


# функция уточнения начальных (допустимых) значений
def refinement_of_initial_values(Xj):
    # добавление значений к начальным
    implementation_values = np.concatenate(
        (implementation_values, Xj), axis=1
        )
