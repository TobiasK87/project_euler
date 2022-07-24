# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:06:43 2017

@author: Tobi
"""

import numpy as np


n = 5

def primes_below_n(n): # including double counting of primes
                  primes = np.array(np.ones((n-1,2)))
                  
                  primes[:,0] = list(range(2,n+1))
                  print(primes)
                  for i in range(n-1):
                      if primes[i,1]==0:
                          continue
                      else:
                          j = 2
                          k = primes[i,0]
                          m = k * j
                          while m <= n:
#                              print(m)
                              primes[m-2,1] == 0
                            
                              j += 1
                              m = k * j
                          print(primes)
                          
                  return primes[primes[:,1]==1,0]
              
primes_below_n(20)

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