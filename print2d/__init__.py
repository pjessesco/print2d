import numpy as np


def _extract_substring_height(string, height):
    h = 0
    end = 0
    if string.count("\n") < height:
        return " " * (string.find("\n") + 1)

    for i in range(len(string)):
        if string[i] == '\n':
            start = end
            end = i + 1
            if height == h:
                return string[start:end - 1] + " "
            h += 1
    return string[end:]


def _generate_main_line(height, str_list, h_list):
    result = ""
    for i in range(len(str_list)):
        if h_list[i] == 1:
            result += str_list[i] + " "
        else:
            result += _extract_substring_height(str_list[i], height) + " "
    return result


def _generate_other_line(height, str_list, w_list, h_list):
    result = ""
    for i in range(len(str_list)):
        if h_list[i] == 1:
            result += " " * (w_list[i] + 1)
        else:
            result += _extract_substring_height(str_list[i], height) + " "
    return result


def _core(args):
    arg_str_list = []
    arg_w_list = []
    arg_h_list = []

    for arg in args:

        # More than 2 dimension numpy array
        if type(arg) == np.ndarray and len(arg.shape) > 2:
            print("More than 3d numpy array is not supported")
            exit(-1)

        # Considering 2d numpy array that height != 1
        elif type(arg) == np.ndarray and len(arg.shape) == 2 and arg.shape[0] != 1:
            str_arg = str(arg)
            arg_str_list.append(str_arg)
            arg_w_list.append(str_arg.index("\n") + 1)
            arg_h_list.append(arg.shape[0])

        else:
            str_arg = str(arg)
            arg_str_list.append(str_arg)
            arg_w_list.append(len(str_arg))
            arg_h_list.append(1)

    output_height = max(arg_h_list)
    result_str_list = [""] * output_height

    plain_text_height = 0

    for w in range(len(args)):
        for h in range(output_height):
            if h == plain_text_height:
                result_str_list[h] = _generate_main_line(h, arg_str_list, arg_h_list)
            else:
                result_str_list[h] = _generate_other_line(h, arg_str_list, arg_w_list, arg_h_list)

    result = ""
    for s in result_str_list:
        result += (s + "\n")
    return result[:-1]

def print2d(*args):
    print(_core(args))
