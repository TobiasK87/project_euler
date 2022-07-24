# -*- coding: utf-8 -*-
"""
Created 30/10/2021 17:50

@author: Tobi
"""


# erath from https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def erath(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

primes = erath(10**7)

dic = {0: [[]], 2: [[2]], 3: [[3]]}
n = 4
max_var = 5000
while True:
    if n%10==0:
        print(n)
    pot = []
    for p in [pr for pr in primes if pr<=n]:
        if(n-p>1 or (n==p and n in primes)):
            for m in dic[n-p]:
                l = m.copy()
                l.extend([p])
                l.sort()
                pot.extend([l])
        pot.sort()
        l = list(pot for pot,_ in itertools.groupby(pot))
    dic[n] = l
    if len(l)>=max_var:
        break
    n+=1
print(n) # 71