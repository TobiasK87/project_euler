# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:45:25 2017

@author: Tobi
"""

a = 1
b = 1
c = 2
n = 2
while len(str(c)) < 1000:
    n += 1
    print(n)
    c = a+b
    a = b
    b = c

print(n) # 4782
print(c)

print(519432**525806 > 632382**518061)

print(ln(2))