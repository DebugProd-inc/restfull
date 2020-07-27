import json
import numpy


def Read_Init_Data():
    with open("Init_data.json", "r") as f:
        Init_data = json.load(f)
        # {[
        # [..],
        # [..],
        # ...,
        # [..]
        # ]}
    Init_data = numpy.array(Init_data, float)
    print(Init_data)
    return Init_data


def Write_Init_Data(Init_X):
    data = Init_X.tolist()
    with open("Init_data.json", "w") as f:
        json.dump(data, f)
        # {[
        # [..],
        # [..],
        # ...,
        # [..]
        # ]}


def Write_result(operation_permit):
    dict_result = {}
    dict_result["operation permit"] = operation_permit
    ''' dict_result["distribution_function_parameters"]
    = distribution_function_parameters.tolist()'''
    with open("Result.json", "w") as f:
        f.write(json.dump(dict_result))


def Write_Math_Data(cov, MU_MAX, X_C):
    dict_result = {}
    dict_result["Cov_matrix"] = cov
    dict_result["MU_MAX"] = MU_MAX
    dict_result["X_C"] = X_C
    with open("MathData.json", "w") as f:
        f.write(json.dump(dict_result))


def Read_Math_Data():
    with open("MathData.json", "r") as f:
        MathData = json.load(f)
        # словарь
    return MathData


def Read_Cur():
    with open("Cur_Parametrs.json", "r") as f:
        Cur = json.load(f)
    return Cur
