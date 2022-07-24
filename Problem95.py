# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 08:43:28 2021

@author: Tobi
"""

import os

# Generate primes
def primes(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3,int(1 + n**0.5),2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r

prime_list = primes(10**6)
prime_list = [i for i,x in enumerate(prime_list) if x]

# create prime_factorizations --> could maybe be done more efficiently by looping over all
# prime powers and adding these to the lists which are the elements of all_prime_factorizations
def prime_factors(n):
    primfac = []
    p = 2
    d = 0
    while p*p <= n:
        while (n % p) == 0:
            primfac.append(p)  # supposing you want multiple factors repeated
            n //= p
        d += 1
        p = prime_list[d]
    if n > 1:
       primfac.append(n)
    return primfac

all_prime_factorizations = {}
for i in range(2,10**6+1):
    if i%10**5==0:
        print(i)
    if i in prime_list:
        all_prime_factorizations[i] = [i]
    else:
        all_prime_factorizations[i] = prime_factors(i)

# save preliminary results
os.getcwd()
os.chdir('C:\\Users\\Tobi\\Programmieren\\Python Scripts\\Project Euler\\Data')
with open('prime_factorizations_below_1e6.csv', 'w') as f:
    for key in all_prime_factorizations.keys():
        f.write("%s,%s\n"%(key,all_prime_factorizations[key]))

# write helper functions that generate all factors of a number based on the prime factorization
def add_powers(n, p, e, factors):
    for i in range(e+1):
        factors.append(n*p**i)
    return(factors)
    

def generate_factors(ls): # ls is a prime factorization list, e.g. [2,2,3,3] for 18
    factors = []
    for p in list(set(ls)):
        new_factors = add_powers(1, p, ls.count(p), [])
        if factors == []:
            factors = new_factors
        else:
            factors = [p*q for p in factors for q in new_factors]
    return(sorted(factors))

# generate all factorizations
factors = {1: [1]}
for n in range(2,10**6):
    factors[n] = generate_factors(all_prime_factorizations[n])

# generate the factor sums
factor_sums = {}
for f in factors.keys():
    factor_sums[f] = sum(factors.get(f, 0)) - f
    
# run through the chains and count how long they are, if it is not a chain, do not save it.
chain = {}
for f in factor_sums.keys():
    if f%10000==0:
        print(f)    
    s = f
    i = 0
    been_there = [s]
    while s>1 and s<=10**6:
        s = factor_sums[s]
        i += 1
        if s==f:
            chain[f] = i
            break
        if s in been_there:
            break
        been_there.append(s)
    
max(chain.values()) # 28
list(chain.keys())[list(chain.values()).index(28)] # 14316

# it is better to get the key as below...
min([k for k,v in chain.items() if v==max(chain.values())]) # 14316
