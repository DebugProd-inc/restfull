import numpy as np
import random
import scipy
import scipy.spatial
import TV_i_MS
import test_values
import functional_check
import mahalanobis_distance as md

X_C = get_center.get_center(xj)
COV_MATRIX = np.cov(xj)


def update_values(Xj):
    global Init_X
    Init_X = np.concatenate(
        (Init_X, Xj), axis=1
        )
    begin(Init_X)


def begin(Xi):
    global Init_X
    global X_C
    global distance
    global Veybull
    Init_X = Xi
    distance = md.mahalanob(Xi, X_C, COV_MATRIX)
    Veybull = TV_i_MS.Class_distribution_func(distance)


def check(confidence_level, Xj):
    global Veybull
    global distance
    MU_max = Veybull.get_quantile(confidence_level)
    flag = functional_check.functional_check(distance, mu_max)
    if (flag):
        update_values(Xj)
    return flag
