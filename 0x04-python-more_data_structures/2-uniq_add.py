#!/usr/bin/python3

def uniq_add(my_list=[]):
    """write function uniq add """
    new_list = set(my_list)
    sum = 0
    for n in new_list:
        sum = sum + n
    return sum
