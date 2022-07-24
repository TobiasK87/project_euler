# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:06:36 2021

@author: Tobi
"""
def totient(x):
    t = x
    for k in [2,  2, 2, 3, 5, 7, 11, 13, 17, 19, 23]:
        t -= t // k
    return t

def r(x):
    return totient(x) / (x - 1)

x = 2 * 2 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23

print(x, r(x))

