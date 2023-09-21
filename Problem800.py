# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 13:20:40 2023

@author: Tobi
"""

import numpy as np
from numpy import log as ln
from math import ceil, floor

p_limit = 2*10**7

# generate list of all primes below n
def primes(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3,int(1 + n**0.5),2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r
prime_list = [i for i,x in enumerate(primes(p_limit)) if x]


smaller_equal_primes = [1]
larger_equal_primes = [2,2]
for last_prime, current_prime in zip(prime_list[:-1], prime_list[1:]):
     smaller_equal_primes.extend((current_prime-last_prime)*[last_prime])
     larger_equal_primes.extend((current_prime-last_prime)*[current_prime])
     
 
dic = dict([(v,k+1) for (k,v) in enumerate(prime_list)])
pi = dict([(i+2,dic[x]) for (i,x) in enumerate(smaller_equal_primes[1:])])
prime_number = dict([(v,k) for (k,v) in enumerate(prime_list)])


def equation(p, q):
    return ln(p)*q + ln(q)*p

def C(n):
    cnt = 0
    lmt = n*np.log(n)

    for _, p in enumerate(prime_list):
        if p*ln(p) > lmt:
            break
        q = larger_equal_primes[ceil(lmt/ln(p))]
        q_upper, q_lower = q, q
        infite_regression_cnt = 0
        while equation(p,q_lower) > lmt:
            q_lower = larger_equal_primes[ceil(q_lower/2)]
        infite_regression_cnt = 0
        while True:
            infite_regression_cnt += 1
            if infite_regression_cnt > 1000:
                print(f"Somehow got stuck in infinite loop for p={p} with q_lower={q_lower} and q_upper={q_upper}")
                break
            q_lower, q_upper = interval_nesting(p, q_lower, q_upper, lmt)
            if equation(p,q_lower) <= lmt and equation(p,prime_list[prime_number[q_lower]+1]) > lmt:
                break
        if p<q_lower:
            cnt += pi[q_lower] - pi[p]
    return cnt
            
                   
        
def interval_nesting(p, q_lower, q_upper, lmt):
    q_new = prime_list[prime_number[q_lower]+floor((prime_number[q_upper]-prime_number[q_lower])/2)]
    if equation(p,q_new) > lmt:
        q_upper = q_new
    else:
        q_lower = q_new
    return q_lower, q_upper
           

print(C(800800)) # 1412403576


