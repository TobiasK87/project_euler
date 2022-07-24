# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 12:30:51 2020

@author: Tobi
"""

import numpy as np

def ggt(m,n):
    if n==0:
        return m
    else:
        return ggt(n, m%n)

cnt = 0
corr = []
for i in range(1,101):
    for j in range(1,i+1):
        for k in range(1,j+1):
            a = np.sqrt(i**2+(j+k)**2)
            if a==int(a):
                corr.append([k,j,i])
                cnt+=1
print(cnt)
corr[:10]

#################

primitive_tripel = []
for i in range(2,101):
    for j in range(1,i):
        if i%2==1 and j%2==1:
            continue
        elif ggt(i,j)>1:
            continue
        primitive_tripel.append(sorted([i**2-j**2,2*i*j,i**2+j**2]))
        
pairs = []
for t in primitive_tripel:
    i=1
    while True:
        a = i*t[0]
        b = i*t[1]
        if b>5000: # had to go at least until 2* the final result
            break
        pairs.append([a,b])
        i+=1
print(len(pairs))

triples = []
for p in pairs:
    a=1
    b = p[0]-1
    c = p[1]
    while a<=b:
        triples.append([a,b,c])
        a += 1
        b += -1
    c= p[0]
    b = c
    a = p[1]-c
    while c>=b and a<=b and a>=1:
        triples.append(sorted([a,b,c]))
        b += -1
        a += 1

len(triples)

res = [a for a in triples if max(a)<=1818] # trial and error yields
print(len(res)) # 1000457 --> 1818