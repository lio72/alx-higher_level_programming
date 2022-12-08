#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ common elements"""
    all_set = set_1.union(set_2)
    new_list = [n for n in all_set if n not in set_2 or n not in set_1]
    return new_list
