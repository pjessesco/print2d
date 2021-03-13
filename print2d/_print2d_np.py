import numpy as np


def np_extract_substring_height(string, height):
    h = 0
    end = 0
    if string.count("\n") < height:
        return " " * (string.find("\n") + 2)

    for i in range(len(string)):
        if string[i] == '\n':
            start = end
            end = i + 1
            if height == h:
                return string[start:end - 1] + "  "
            h += 1
    return string[end:] + " "


def parse_numpy(np_arr):
    assert type(np_arr) == np.ndarray
    dim = len(np_arr.shape)
    if dim > 2:
        print("Given NumPy array's dimension is larger than 2, which is not supported.")
        exit(-1)
    elif dim == 2:
        if np_arr.shape[0] == 1:
            return len(str(np_arr)), 1
        else:
            return str(np_arr).index("\n") + 1, np_arr.shape[0]
    else:
        print("parse_numpy() : unexpected error")
        exit(-1)
