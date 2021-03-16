import numpy as np
import logging

def np_extract_substring_height(np_arr, target_line):
    current_line = 0
    end = 0
    string = str(np_arr)
    if string.count("\n") < target_line:
        return " " * (string.find("\n") + 2)

    for i in range(len(string)):
        if string[i] == '\n':
            start = end
            end = i + 1
            if target_line == current_line:
                return string[start:end - 1] + "  "
            current_line += 1
    return string[end:] + " "


def parse_numpy(np_arr):
    assert type(np_arr) == np.ndarray
    dim = len(np_arr.shape)
    if dim > 2:
        logging.error("Given NumPy array's dimension is larger than 2, which is not supported : ",np_arr)
        exit(-1)
    elif dim == 2:
        if np_arr.shape[0] == 1:
            return len(str(np_arr)), 1
        else:
            return str(np_arr).index("\n") + 1, np_arr.shape[0]
    else:
        logging.error("parse_numpy() : unexpected error")
        exit(-1)
