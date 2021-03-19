from ._print2d_np import *
from ._print2d_torch import *
from ._print2d_list import *

import logging


def parse_string(string):
    return len(str(string)), 1


def _core(args):
    arg_w_list = []
    arg_h_list = []

    # Parse width, height if arg has 1 or 2 dimension
    # If arg has more than 2 dimension, error will be occured in each parse_XX function.
    for arg in args:
        if is_type_np(type(arg)):
            width, height = parse_numpy(arg)
        elif is_type_torch(type(arg)):
            width, height = parse_torch(arg)
        elif is_type_list(type(arg)):
            width, height = parse_list(arg)
        else:
            width, height = parse_string(arg)

        assert width is not None and height is not None
        arg_w_list.append(width)
        arg_h_list.append(height)

    output_line = max(arg_h_list)
    plain_text_line = 0
    result_str_list = [""] * output_line

    for i in range(len(args)):
        width = arg_w_list[i]
        height = arg_h_list[i]
        arg = args[i]

        for line in range(output_line):
            # Considering plain text or array with height 1
            if height == 1:
                if line == plain_text_line:
                    result_str_list[line] += (str(arg) + " ")
                else:
                    result_str_list[line] += " " * (width + 1)

            # Considering 2d-printed objects
            else:
                if is_type_np(type(arg)):
                    result_str_list[line] += np_extract_substring_height(arg, line)
                elif is_type_torch(type(arg)):
                    result_str_list[line] += torch_extract_substring_height(arg, line)
                elif is_type_list(type(arg)):
                    result_str_list[line] += list_extract_substring_height(arg, line, width)
                else:
                    logging.error("Unknown 2d array type : ", type(arg))
                    exit(-1)

    result = ""
    for s in result_str_list:
        result += (s + "\n")
    return result[:-1]

def print2d(*args):
    print(_core(args))
