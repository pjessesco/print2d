import logging


def is_type_torch(obj_type):
    return str(obj_type) == "<class 'torch.Tensor'>"


def torch_extract_substring_height(torch_arr, target_line):
    current_line = 0
    end = 0
    string = str(torch_arr)
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


def parse_torch(tensor):
    assert is_type_torch(type(tensor))
    dim = len(tensor.shape)
    if dim > 2:
        logging.error("Given torch tensor's dimension is larger than 2, which is not supported : ", tensor)
        exit(-1)
    elif dim == 2:
        if tensor.shape[0] == 1:
            return len(str(tensor)), 1
        else:
            return str(tensor).index("\n") + 1, tensor.shape[0]
    else:
        logging.error("parse_torch() : unexpected error")
        exit(-1)

