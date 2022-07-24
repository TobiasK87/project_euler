# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 20:18:56 2017

@author: Tobi
"""

combs=[]
for i1 in range(2):    
    for i2 in range(3):
        for i3 in range(5):
            print(i1,i2,i3)
            for i4 in range(11):
                for i5 in range(21):
                    for i6 in range(41):
                        for i7 in range(101):
                            for i8 in range(201):
                                s = 200 * i1 + 100 * i2 + 50 * i3 + 20 * i4 + 10 * i5 + 5 * i6 + 2 * i7 + 1 * i8
                            if s == 200:
                                comb = [i1,i2,i3,i4,i5,i6,i7,i8]
                                combs.append(comb)    
                                
print(combs[:200])
len(combs)