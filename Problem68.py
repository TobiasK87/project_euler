# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 15:18:28 2019

@author: Tobi
"""

def combs(length):
    ls=[]
    for i in range(1,11):
        for j in range(1,11):
            for k in range(1,11):
                if i+j+k==length and not i==j and not i==k and not j==k:
                    ls.append([i,j,k])
    ls = [i for i in ls if 10 not in i or i[0]==10]
    return ls

ls = combs(14)
hits=[]

for i1 in range(len(ls)):
    t1 = ls[i1]
    for i2 in range(i1):
        t2 = ls[i2]
        if t1[2]!=t2[1]:
            continue
        for i3 in range(i2):
            t3 = ls[i3]
            if t2[2]!=t3[1]:
                continue
            for i4 in range(i3):
                t4 = ls[i4]
                if t3[2]!=t4[1]:
                    continue
                for i5 in range(i4):
                    t5 = ls[i5]
                    if t4[2]!=t5[1] or t5[2]!=t1[1]:
                        continue
                    if sorted(list(set([t1[0],t2[0],t3[0],t4[0],t5[0]])))!=sorted([t1[0],t2[0],t3[0],t4[0],t5[0]]):
                        continue
                    hits.append([t1,t2,t3,t4,t5])

# print(hits)

hits_clean=[]
for h in hits:
    for i in h:
        if 10 in i:
            hits_clean.append(h)
#print(hits_clean)
for h in hits_clean:
    print(h)

# händisch alle durchlaufen lassen für combs(13)-combs(20) und gesehen, dass
# [[10, 3, 1], [9, 1, 4], [8, 4, 2], [7, 2, 5], [6, 5, 3]] bzw. anfangend mit dem kleinsten
# external node 6531031914842725 die Lösung ist