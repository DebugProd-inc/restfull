import numpy as np
from test_values import confidence_probability

# получение из выборки расстояний Махаланобиса при штатном
# функционировании квантили заднного уровня


def get_quantile(dj):
    return np.quantile(dj, confidence_probability)
