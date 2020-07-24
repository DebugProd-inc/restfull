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


def Write_result(operation_permit, refusal_parameter_number, distribution_function_parameters, distance_cur_parameters):
    dict_result = {}
    dict_result["operation permit"] = operation_permit
    dict_result["refusal_parameter_number"] = refusal_parameter_number
    dict_result["distribution_function_parameters"] = distribution_function_parameters.tolist()
    dict_result["distance_cur_parameters"] = distance_cur_parameters.tolist()
    with open("Result.json", "w") as f:
        f.write(json.dump(dict_result))
