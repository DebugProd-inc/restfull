from test_values import IMPLEMENTATION_VALUES
from get_center import get_center
from quantile import get_quantile
from mahalanobis_distance import mahalanob
from functional_check import *
from dispersion import get_dispersion

# пример вычисления координат геометрического центра
X_C = get_center(IMPLEMENTATION_VALUES)

# пример вычисления максимально допустимого расстояния Махаланобиса
MU_MAX = get_quantile(mahalanob(IMPLEMENTATION_VALUES))
