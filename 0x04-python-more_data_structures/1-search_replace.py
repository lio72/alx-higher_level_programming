#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """search and replace"""
    new_list = [replace if n == search else n for n in my_list]
    return new_list
