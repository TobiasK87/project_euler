# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 18:16:37 2017

@author: Tobi
"""

import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

A = set([1,2,3,4,5])

B = findsubsets(A,3)



def is_special_sumset(A):
    n = len(A)
    special = 1
    for i in range(1,n):
        if special == 0:
            break
        subsets = findsubsets(A,i)
        for B in subsets:
            B = set(B)
            A_min_B = set(A - B)
            a_min_b = len(A_min_B)
            for j in range(1,a_min_b+1):
                C_Pot = findsubsets(A_min_B,j)
                for C in C_Pot:
                    C = set(C)
                    b = len(B)
                    c = len(C)
                    if sum(B) == sum(C):
                        special = 0
                        #                print('hier1')
                        break
                    if c > b and sum(C) <= sum(B):
                        special = 0
                        #                print('hier2')
                        break
    return special


A = set([20, 31, 38, 39, 40, 42, 45])
print(sum(A)) # 255
print(is_special_sumset(A)) # obere Schranke

min_sum = 255
best_set = A
for i1 in range(19,20):
    print('i1:',i1)
    for i2 in range(i1+1,40):
        print('i2:',i2)
        for i3 in range(i2+1,45):
            print(i3)
            for i4 in range(i3+1,46):
                for i5 in range(i4+1,47):
                    for i6 in range(i5+1,48):
                        for i7 in range(i6+1,49):
                            A = set([i1,i2,i3,i4,i5,i6,i7])
                            summe = sum(A)
                            if summe >= min_sum:
                                break
                            elif is_special_sumset(A)==1:
                                best_set = A
                                min_sum = summe
                                print('New Min SUM:', min_sum)

print(min_sum) # führt zu nichts.. 255 ist immer noch optimum
print(best_set)
print(is_special_sumset(best_set))
     
     
     

A = set([2,3,4])
print(is_special_sumset(A))

A = set([1,2,3])
print(is_special_sumset(A))