# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 08:40:46 2021

@author: Tobi
"""

import numpy as np

def factorization_to_k(ls):
    return np.prod(ls) - np.sum(ls) + len(ls)

dic = {}
Limit = 12000

def iterate_loops(num, ls, depth):
    if ls == []:
        start = 2
    else:
        start = min(ls)
    for i in range(start, 2*Limit+1):
        if depth==1:
            print("depth, i", depth, i)
        num *= i
        if num > Limit*2+1:
            return
        ls.append(i)
        iterate_loops(num, ls, depth+1)
        k = factorization_to_k(ls)
        if len(ls)>1 and (dic.get(k) is None or dic.get(k) > num):
            dic[k] = num
        ls.pop()
        num = int( num/i)
            
iterate_loops(1, [], 1)

full_list = [dic[key] for key in dic if key <= Limit]
np.sum(list(set(full_list))) # 7587457