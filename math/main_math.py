import numpy as np
import random
import scipy
import scipy.spatial
import TV_i_MS
import test_values
import functional_check


def update_values(Xj):
    global Init_X
    Init_X = np.concatenate(
        (Init_X, Xj), axis=1
        )
    begin(Init_X)


X_C = get_center.get_center()


def begin(Xi):
    global Init_X
    global X_C
    global distance
    global Veybull
    Init_X = Xi
    X_C = get_center.get_center(Xi)
    distance = mahalanob(Xi)
    Veybull = TV_i_MS.Class_distribution_func(distance)


def check(confidence_level, Xj):
    global Veybull
    global distance
    MU_max = Veybull.get_quantile(confidence_level)
    flag = functional_check.functional_check(distance, mu_max)
    if (flag):
        update_values(Xj)
    return flag
