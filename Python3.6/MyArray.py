# Filename: MyArray.py
# Function description: Array and its operating
# --------------------------------

import types
import numpy


class MyArray(object):
    """
    All the element in this array must be numbers
    """
    __value = []
    __size = 0

    def __is_numeber(self, n):
        if type(n) != complex and type(n) != float \
                and type(n) != int and type(n) != :
            return False
        return True
