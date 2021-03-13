import torch


def torch_extract_substring_height(string, height):
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


def parse_torch(tensor):
    assert type(tensor) == torch.Tensor
    dim = len(tensor.shape)
    if dim > 2:
        print("Given torch tensor's dimension is larger than 2, which is not supported.")
        exit(-1)
    elif dim == 2:
        if tensor.shape[0] == 1:
            return len(str(tensor)), 1
        else:
            return str(tensor).index("\n") + 1, tensor.shape[0]
    else:
        print("parse_torch() : unexpected error")
        exit(-1)

