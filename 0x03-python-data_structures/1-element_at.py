#!/usr/bin/python3
def element_at(my_list, idx):
    """print element of list with index"""
    if idx in list(range(0, len(my_list))):
        return my_list[idx]
    else:
        return None
