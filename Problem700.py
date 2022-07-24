# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 12:11:32 2020

@author: Tobi
"""
a = 1504170715041707
d = 4503599627370517

def extgcd(a, b):
    if b==0:
        return a, 1, 0
    else:
        g, u, v = extgcd(b, a%b)
        q=a//b
        return g, v, u-q*v

a_inv = extgcd(a,d)[1]%d

sm = a
mn = a
for i in range(1,10**8):
    k = (a*i)%d
    if k<mn:
        print(k)
        mn=k
        sm+=k

mn2 = (1*a_inv)%d
for i in range(2,mn):
    k = (i*a_inv)%d
    if k < mn2:
        mn2=k
        sm+=i
print(sm+1) # 1 in definitely a Eulercoin