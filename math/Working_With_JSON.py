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
    data = Init_data.tolist()
    with open("Init_data.json", "w") as f:
        f.write(json.dump(data))
        # {[
        # [..],
        # [..],
        # ...,
        # [..]
        # ]}


# def Write_result()
