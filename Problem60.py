# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
#            print(((n-i*i-1)/(2*i)+1))
            sieve[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

primes = primes(10**6)


def both_prime(p,q):
    result = 0
    n = int(str(p)+str(q))
    if n in primes:
        n = int(str(q)+str(p))
        if n in primes:
            result = 1
    return result

both_prime(3,5)
solution = []
for i1 in range(4,len(primes)):
    print(i1)
    for i2 in range(3,i1):
        for i3 in range(2,i2):
            for i4 in range(1,i3):
                for i5 in range(i4):
                    p1 = primes[i1]
                    p2 = primes[i2]
                    p3 = primes[i3]
                    p4 = primes[i4]
                    p5 = primes[i5]
                    ls = [p1,p2,p3,p4,p5]
                    r = 0
                    for S in findsubsets(ls,2):
                        
                        r += both_prime(S[0],S[1])
                    if r == 10:
                        solution = ls
    if solution != []:
        break
print(solution)





S = [1,2,3,4,5]            
findsubsets(S,2)