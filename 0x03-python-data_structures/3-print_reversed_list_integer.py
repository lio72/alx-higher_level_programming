#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Print reserved list"""
    if my_list:
        i = len(my_list)
        while i > 0:
            i = i - 1
            print("{:d}".format(my_list[i]))
