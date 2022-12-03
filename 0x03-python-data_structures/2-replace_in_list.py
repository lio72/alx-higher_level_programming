#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace value in list"""
    if idx in list(range(0, len(my_list))):
        my_list.insert(idx, element)
        return my_list
