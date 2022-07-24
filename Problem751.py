# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:27:15 2021

@author: Tobi
"""

from decimal import *
import numpy as np
getcontext().prec = 26

def create_sequence(x):
    a = [str(int(np.floor(x))) + "."]
    b_new = Decimal(x)
    # b = [b_new]
    for i in range(1,25):
        b_floor = int(np.floor(b_new))
        b_new = Decimal(b_floor) * (Decimal(b_new) - Decimal(b_floor) + 1)
        # b.append(b_new)
        a_new = int(np.floor(b_new))
        a.append(str(a_new))
    return(''.join(a))

tol = 25
# i = 1
x = 2.2
t = 2.3
while abs(float(Decimal(t) - Decimal(x)))>10**(-tol):
    x = Decimal(t)/2 + Decimal(x/2)
    t = create_sequence(x)
    # i += 1
    # if i%1000==0:
    #   print("i, diff", i, Decimal(t) - Decimal(x))

str(x)[:26] # 2.223561019313554106173177
