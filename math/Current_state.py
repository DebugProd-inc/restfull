import Working_With_JSON
import mahalanobis_distance as md
import functional_check as f
import numpy as np

MathData = Working_With_JSON.Read_Math_Data()
COV_MATRIX = np.array(MathData["Cov_matrix"])  # возможны проблемы
MU_MAX = MathData["MU_MAX"]
X_C = np.array(MathData["X_C"])
X = Working_With_JSON.Read_Cur()

distance = mahalanobis_distance.mahalanob(x, X_C, COV_MATRIX)

flag = f.functional_check(distance, MU_MAX)
Write_result(flag)
