# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 22:48:54 2021

@author: Tobi
"""

limit = 999

def sum_of_multiples_below_limit(n, limit):
    return(int(limit//n * (limit//n + 1) / 2) * n)

sum_of_multiples_below_limit(3, limit) + sum_of_multiples_below_limit(5, limit) - sum_of_multiples_below_limit(15, limit)
# 233168