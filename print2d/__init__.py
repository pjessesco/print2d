import numpy as np
from ._print2d_np import *

import torch
from ._print2d_torch import *


def parse_string(string):
    return len(str(string)), 1


def _core(args):
    arg_w_list = []
    arg_h_list = []

    for arg in args:
        if type(arg) == np.ndarray:
            width, height = parse_numpy(arg)
        elif type(arg) == torch.Tensor:
            width, height = parse_torch(arg)
        else:
            width, height = parse_string(arg)

        assert width is not None and height is not None
        arg_w_list.append(width)
        arg_h_list.append(height)

    output_line = max(arg_h_list)
    plain_text_line = 0
    result_str_list = [""] * output_line

    for i in range(len(args)):
        string = str(args[i])
        width = arg_w_list[i]
        height = arg_h_list[i]

        for line in range(output_line):
            # Considering plain text or array with height 1
            if height == 1:
                if line == plain_text_line:
                    result_str_list[line] += (string + " ")
                else:
                    result_str_list[line] += " " * (width + 1)

            # Considering 2d-printed objects
            else:
                if type(arg) == np.ndarray:
                    result_str_list[line] += np_extract_substring_height(string, line)
                elif type(arg) == torch.Tensor:
                    result_str_list[line] += torch_extract_substring_height(string, line)
                else:
                    print("Unexpected error : it should not be printed, please report issue")
                    exit(-1)

    result = ""
    for s in result_str_list:
        result += (s + "\n")
    return result[:-1]

def print2d(*args):
    print(_core(args))
