import numpy as np
import random
import scipy
import scipy.spatial
import TV_i_MS
import test_values
import functional_check
import mahalanobis_distance as md
import get_center
import Working_With_JSON


# получение центра, ковариационной матрицы и параметров функции распределения
# xj - матрица исходных данных штатного функционирования
'''
def reference_parameters(xj):
    global X_C
    global COV_MATRIX
    global PARAMETRS
    X_C = get_center.get_center(xj)
    COV_MATRIX = np.cov(xj)
    tvims = TV_i_MS.Class_distribution_func(md.mahalanob(xj, X_C, COV_MATRIX))
    PARAMETRS = tvims.parameters
'''

'''def update_values(Xj):
    global Init_X
    Init_X = np.concatenate(
        (Init_X, Xj), axis=1
        )
    begin(Init_X)
'''
'''
def begin(Xi):
    global Init_X
    global X_C
    global distance
    global Veybull
    Init_X = Xi
    distance = md.mahalanob(Xi, X_C, COV_MATRIX)
    Veybull = TV_i_MS.Class_distribution_func(distance)
'''
'''######
def check(confidence_level, Xj):
    global Veybull
    global distance
    MU_max = Veybull.get_quantile(confidence_level, PARAMETRS)
    flag = functional_check.functional_check(distance, mu_max)
    if (flag):
        update_values(Xj)
    return flag
'''

Init_X = Working_With_JSON.Read_Init_Data()
X_C = get_center.get_center(Init_X)
COV_MATRIX = np.cov(Init_X)
tvims = TV_i_MS.Class_distribution_func(md.mahalanob(Init_X, X_C, COV_MATRIX))
MU_MAX = tvims.get_quantile(0.95)
Working_With_JSON.Write_Math_Data(COV_MATRIX, MU_MAX, X_C)
# запись в файл данных для проверки текущего состояния
