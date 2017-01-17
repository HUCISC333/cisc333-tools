#!/usr/bin/env python
"""Stuff"""
import random
from time import ctime

class Account:
    """This ia constructor"""
    def __init__(self, my_id):
        self.my_id = my_id
        my_id = 666


    """This is a class function. Functions in a class require the first """
    def random_num(self, x=None):
        if x is None:
            x = ctime()

        random.seed(x)
        return random.randint(1,10)


acc = Account(123)
print acc.my_id
print acc.random_num()
