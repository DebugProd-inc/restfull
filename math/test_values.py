import numpy as np
import random

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

# уровень вероятности безперебойной работы ВС
confidence_probability = 0.95
