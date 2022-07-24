# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:00:25 2017

@author: Tobi
"""

s = 1
k=1
i=1
while True:
    for j in range(0,4):
        i += 2*k
        print(i)
        s += i
    k += 1
    if k==501:
        break
    
print(s)