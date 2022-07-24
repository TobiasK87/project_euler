# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:32:50 2021

@author: Tobi
"""

import numpy as np

def partitions(s):
    if len(s) > 0:
        for i in range(1, len(s)+1):
            first, rest = s[:i], s[i:]
            for p in partitions(rest):
                yield [first] + p
    else:
        yield []
 
    
Limit = 10**6
T = []
for n in range(1,Limit+1):
    if n%10000==0:
        print(n)
    part = list(partitions(str(n**2)))     
    for p in part:
        a = [int(s) for s in p if len(p)>1]
        #print(a)
        if np.sum(a)==n:
            T.append(n**2)
            break
sum(T)
        #sums = [np.sum(a) for a]
        #print(sums)
    
    
[s for s in list(partitions("1234")) for int(i) in s ]

string_list = ["1", "2", "3"]

integer_map = map(int, string_list)

integer_list = list(integer_map)

np.sum([])

1+1

1+1+1
1+2
2+1

1+1+1+1
1+1+2
1+2+1
2+1+1
1+3
3+1
2+2


1+1+1+1+1
1+1+1+2
1+1+2+1
1+2+1+1
2+1+1+1
1+1+3
1+3+1
3+1+1




1+1+1+1+1+1
len(str(5)+ str(6))

1+1+2

T = []

for i1 in range(0,10**5):
    if i1%100==0:
        print(i1)
    for i2 in range(0,10**5):
        s = str(i1)+str(i2)
        if len(s)>6:
            break
        for i3 in range(0,10**5):
            s = str(i1)+str(i2) + str(i3)
            if len(s)>6:
                break
            for i4 in range(0,10**5):
                s = str(i1) + str(i2) + str(i3) + str(i4)
                if len(s)>6:
                    break
                for i5 in range(0,10**5):
                    s = str(i1) + str(i2) + str(i3) + str(i4) + str(i5)
                    if len(s)>6:
                        break
                    for i6 in range(0,10**5):
                        s = str(i1) + str(i2) + str(i3) + str(i4) + str(i5) + str(i6)
                        if len(s)>6:
                            break
                        n = i1+i2+i3+i4+i5+i6
                        if n**2==int(s):
                            T.append(n**2)
                            
T

e = 5
T = []

for i1 in range(0,10**e):
    for i2 in range(0,10**e):
        s = str(i1)+str(i2)
        if len(s)>e+1:
            break
        n = i1+i2
        if n**2==int(s):
            T.append(n**2)
        for i3 in range(0,10**e):
            s = str(i1)+str(i2) + str(i3)
            if len(s)>e+1:
                break
            n = i1+i2+i3
            if n**2==int(s):
                T.append(n**2)
            for i4 in range(0,10**e):
                s = str(i1)+str(i2) + str(i3) + str(i4)
                if len(s)>e+1:
                    break
                n = i1+i2+i3+i4
                if n**2==int(s):
                    T.append(n**2)
                for i5 in range(0,10**e):
                    s = str(i1)+str(i2) + str(i3) + str(i4) + str(i5)
                    if len(s)>e+1:
                        break
                    n = i1+i2+i3+i4+i5
                    if n**2==int(s):
                        T.append(n**2)
                    for i6 in range(0,10**e):
                        s = str(i1)+str(i2) + str(i3) + str(i4) + str(i5) + str(i6)
                        if len(s)>e+1:
                            break
                        n = i1+i2+i3+i4+i5+i6
                        if n**2==int(s):
                            T.append(n**2)

T_copy = sorted(list(set(T)))

sum([t for t in T_copy if t>1 and t<1000001])

sum(T_copy)-1+10**6

T_copy = T.copy


45**2 = 2025



def partitions(s):
    if len(s) > 0:
        for i in range(1, len(s)+1):
            #if i<len(str(int(int(s)**0.5)))-1:
             #   continue
            if i>len(str(int(int(s)**0.5)))+1:
                break
            first, rest = s[:i], s[i:]
            for p in partitions(rest):
                yield [first] + p
    else:
        yield []
        
        
def partitions(s):
    ls = []
    if len(s)>0:
        for i in range(1,len(s)+1):
            first, rest = s[:i], s[i:]
            for p in partitions(rest):
                ls.append([first] + p)
        return(ls)
    else:
        return []
    
partitions('2025')
        
Limit = 10**6
T = []
for n in range(1,Limit+1):
    if n%10000==0:
        print(n)
    part = list(partitions(str(n**2)))
    part = [p for p in part if max([len(a) for a in p]) + 1 >= len(str(n))]
    for p in part:
        #if max([len(a) for a in p])+1<len(str(n)):
            #break
        a = [int(s) for s in p if len(p)>1]
        #print(a)
        if np.sum(a)==n:
            T.append(n**2)
            break
sum(T)

temp = list(partitions("999818008281"))
[t for t in temp for a in t if max(len(a))+1<len(str(int(999818008281**0.5)))]

[t for t in temp if max([len(a) for a in t])+1>=len(str(int(999818008281**0.5)))]


[p for k in p for p in part if max(len(k))>=len(str(n))]