import tensorflow as tf
import logging


# Helper function that decides whether input_list is 2d array as expected.
# 1. input_list must be a list.
# 2. Every element of the input_list must be a list and has a same length.
# 3. Every element of the element of the input_list must not be a list
# If all condition met, return True. Otherwise, return False
# This function also returns the longest element's string length used in calculating padding
def is_list_2d(input_list):

    # 1. input_list must be a list.
    if type(input_list) != list:
        logging.error("Given input is not an array : ", input_list)
        return False, -1

    longest_elem_len = 0

    # 2. Every element of the input_list must be a list and has a same length.
    for i in range(0, len(input_list)):
        # 2.1 Check whether the i'th element of input_list is list
        if type(input_list[i]) != list:
            logging.error("One of the element in given array is not a list : ", input_list[i])
            return False, -1
        # 2.2 Check whether the i'th list has same length with i-1'th
        if i != 0 and len(input_list[i-1]) != len(input_list[i]):
            logging.error("Given array's elements have different width. Expected : ", len(input_list[i-1]), "Actual : ", len(input_list[i]))
            return False, -1
        # 3. Every element of the element of the input_list must not be a list
        for elem in input_list[i]:
            if type(elem) == list:
                logging.error("Given array has larger than 2 dimension : ", input_list[i])
                return False, -1
            if len(str(elem)) > longest_elem_len:
                longest_elem_len = len(str(elem))

    return True, longest_elem_len


# Helper function that decides whether input_list is 1d array as expected.
# 1. input_list must be a list.
# 2. Every element of the input_list must not be a list
# If all condition met, return True. Otherwise, return False
def is_list_1d(input_list):
    # 1. input_list must be a list.
    if type(input_list) != list:
        logging.error("Given input is not an array : ", input_list)
        return False
    for elem in input_list:
        if type(elem) == list:
            return False
    return True



def list_extract_substring_height(list_arr, target_line, line_width):

    if target_line >= len(list_arr):
        return " " * (line_width + 1)

    # Calculate padding using given list and width
    word_count = len(list_arr[0])
    word_len = int(((line_width - 2) / word_count) - 2)

    result = " ["
    for elem in list_arr[target_line]:
        result += str(elem).rjust(word_len, " ")+", "

    result = result[:-2]+"]  "

    if target_line == 0:
        result = "[" + result[1:]

    if target_line == len(list_arr)-1:
        result = result[:-2] + "] "

    return result


def parse_list(input_list):

    assert type(input_list) == list
    if is_list_1d(input_list):
        return len(str(input_list)), 1

    is_2d, word_len = is_list_2d(input_list)
    if not is_2d:
        exit(-1)

    word_count = len(input_list[0])
    total_width = word_count * (word_len + 2) + 2

    return total_width, len(input_list)
