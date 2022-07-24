# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:56:50 2021

@author: Tobi
"""

from itertools import repeat

def prime_factorizations_for_all(n):
    ls = [[] for i in repeat(None, n)]
    for p in [p for p in primes if p<=n**0.5]:
        for k in range(p-1,n,p):
            temp = ls[k].copy()
            temp.extend([p])
            ls[k] = temp
    return ls

prime_factorizations_for_all(15)

import primefac
import sys

# n = int( sys.argv[1] )
dic = {}
limit = 24000
for i in range(limit):
    dic[i] = list(primefac.primefac(i))
    
    
# dic[999873]

list(primefac.primefac(3534))