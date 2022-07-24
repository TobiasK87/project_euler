# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:36:37 2020

@author: Tobi
"""

ls=[8,16,27,32,64,81]
sum=0
for i in ls:
    sum+=100//i
print(sum+100)

ls = []
for i in range(2,22):
    e = 3
    while True:
        n=i**e
        if n>10000:
            break
        e+=1
        ls.append(n)

sorted(ls)

ls = list(set(ls))
ls.extend([2**4*3**3,2**5*3**3,2**6*3**3,2**7*3**3,2**8*3**3,2**3*3**4,2**3*3**5,2**3*3**6,2**4*5**3,2**5*5**3,2**6*5**3,2**3*5**4,2**4*7**3])
ls = sorted(ls)


from itertools import combinations
a=list(combinations([2,3,5,7],3))
from functools import reduce
[c=reduce(lambda x,y:x*y,b) for b in a if c<100]


for

print(ls)
sum=0
for i in ls:
    sum+=10000//i
print(sum+10000)

def problem694(n):
    
    return n+