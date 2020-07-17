from test_values import implementation_values
from get_center import get_center
from quantile import get_quantile
from mahalanobis_distance import mahalanob
from functional_check import *
from dispersion import get_dispersion
from update_values import refinement_of_initial_values

# пример вычисления координат геометрического центра
X_C = get_center(implementation_values)

# пример вычисления максимально допустимого расстояния Махаланобиса
MU_MAX = get_quantile(mahalanob(implementation_values))
