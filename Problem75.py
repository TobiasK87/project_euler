# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:34:24 2019

@author: Tobi
"""

L_max = 1500000
Ls=[]
triples = []
cnt = 0

for u in range(1,int(L_max**0.5)):
    if u%100==0:
        print(u)
    for v in range(1,u):
        x = u**2-v**2
        y = 2*u*v
        z = u**2+v**2
        L = x+y+z
        if L <= L_max and L not in Ls:
            Ls.extend([L])
            cnt +=1
        triples.append([x,y,z])
print(cnt)

# jetzt noch ggf nicht-primitive addieren
b=0
for p in Ls:
    if b%1000==0:
        print(b)
    for n in range(1,125001):
        a = n*p
        if a > 15000000:
            break
        if a not in Ls:
            cnt+=1
    b +=1

len(Ls)
cnt