# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 21:41:53 2017

@author: Tobi
"""

ls = []
s = 0
i = 0
e = 0
while True:
    l = len(str(i))
    s += l
    i += 1
    if s > 10**e:
        e += 1
        ls.extend([s-l,i-1])
    if s > 10**6:
        break
    
print(ls) # [1, 1, 10, 10, 100, 55, 1000, 370, 9998, 2777, 100000, 22222, 1000000, 185185]
# --> das gesuchte Produkt ist 1 * 1 *5 * 3 * 7 * 2 * 1 = 210