# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 20:25:27 2019

@author: Tobi
"""
import numpy as np

def primes(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3,int(1 + n**0.5),2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r

prime_list = primes(10**7)
prime_list = [i for i,x in enumerate(prime_list) if x]

primes_small = prime_list[:11301]
       
def prime_factors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

save = []
for i in range(1,120001):
    if i%10**4==0:
        print(i)
    save.append(prime_factors(i))
    
save_unique = [set(s) for s in save] 

rads = [int(np.prod(list(a))) for a in save_unique]

abc_hit=[]
Limit = 120000
C = []
for c in range(1,Limit):
    if not save[c-1] == sorted(list(set(save[c-1]))):
        C.extend([c])
     

# WORKS
for c in C:
    if c%10**3==0:
        print(c)
    #if c%2==0:
    for a in range(1,c+1):
        b = c-a
        if b<a:
            break
        if rads[a-1]*rads[b-1]*rads[c-1]>=c:
            continue
        if save_unique[a-1].intersection(save_unique[b-1])!=set():
            continue
        abc_hit.append([a,b,c])

sum([c[2] for c in abc_hit]) # 18407904. dauert aber eigentlich deutlich zu lange (~15min)




import km
from kdecs import timing

@timing
def p127():
    s, mx = 0, 120000
    rad = {k:km.rad(k) for k in xrange(1, mx+1)}
    radlist = sorted((v,k) for k,v in rad.iteritems())
    for c in xrange(3, mx+1):
        radc, chalf = rad[c], c//2
        for (rada,a) in radlist:
            radac = rada*radc
            if radac>=chalf:
                break
            if a>chalf:
                continue
            b = c-a
            radb = rad[b]
            radabc = radb*radac
            if radabc<c and km.gcd(rada, radb)==1:
                s += c
p127()
print(s)

