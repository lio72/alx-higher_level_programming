#!/usr/bin/python3
def no_c(my_string):
    """remove specifie character in string"""
    if my_string:
        i = 0
        for s in my_string:
            if s in "cC":
                del my_string[i]
            i = i + 1
        return my_string
