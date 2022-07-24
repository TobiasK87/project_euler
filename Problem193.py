# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:45:28 2021

@author: Tobi
"""

def erath(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

primes = erath(2**25)

limit = 2**50
ls = [True]*limit
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0

for i1 in primes:
    s1 += limit//(i1**2)

for i1 in primes:
    if primes.index(i1) % 100 == 0:
        print(i1)
    for i2 in [p for p in primes if p>i1]:
        pr = i1*i2
        if(i1*i2>limit**0.5):
            break
        s2 += limit//(pr**2)
print("s2 done")

for i1 in primes:
    if primes.index(i1) % 100 == 0:
        print(i1)
    for i2 in [p for p in primes if p>i1]:
        if(i1*i2>limit**0.5):
            break
        for i3 in [p for p in primes if p>i2]:
            pr = i1*i2*i3
            if(pr>limit**0.5):
                break
            s3 += limit//(pr**2)
print("s3 done")

for i1 in primes:
    for i2 in [p for p in primes if p>i1]:
        if(i1*i2>limit**0.5):
            break
        for i3 in [p for p in primes if p>i2]:
            if(i1*i2*i3>limit**0.5):
                break
            for i4 in [p for p in primes if p>i3]:
                pr = i1*i2*i3*i4
                if(pr>limit**0.5):
                    break
                s4 += limit//(pr**2)
print("s4 done")

for i1 in primes:
    for i2 in [p for p in primes if p>i1]:
        if(i1*i2>limit**0.5):
            break
        for i3 in [p for p in primes if p>i2]:
            if(i1*i2*i3>limit**0.5):
                break
            for i4 in [p for p in primes if p>i3]:
                if(i1*i2*i3*i4>limit**0.5):
                    break
                for i5 in [p for p in primes if p>i4]:
                    pr = i1*i2*i3*i4*i5
                    if(pr>limit**0.5):
                        break
                    s5 += limit//(pr**2)
print("s5 done")

for i1 in primes:
    for i2 in [p for p in primes if p>i1]:
        if(i1*i2>limit**0.5):
            break
        for i3 in [p for p in primes if p>i2]:
            if(i1*i2*i3>limit**0.5):
                break
            for i4 in [p for p in primes if p>i3]:
                if(i1*i2*i3*i4>limit**0.5):
                    break
                for i5 in [p for p in primes if p>i4]:
                    if(i1*i2*i3*i4*i5>limit**0.5):
                        break
                    for i6 in [p for p in primes if p>i5]:
                        pr = i1*i2*i3*i4*i5*i6
                        if(pr>limit**0.5):
                            break
                        s6 += limit//(pr**2)
print("s6 done")


for i1 in primes:
    for i2 in [p for p in primes if p>i1]:
        if(i1*i2>limit**0.5):
            break
        for i3 in [p for p in primes if p>i2]:
            if(i1*i2*i3>limit**0.5):
                break
            for i4 in [p for p in primes if p>i3]:
                if(i1*i2*i3*i4>limit**0.5):
                    break
                for i5 in [p for p in primes if p>i4]:
                    if(i1*i2*i3*i4*i5>limit**0.5):
                        break
                    for i6 in [p for p in primes if p>i5]:
                        if(i1*i2*i3*i4*i5*i6>limit**0.5):
                            break
                        for i7 in [p for p in primes if p>i6]:
                            pr = i1*i2*i3*i4*i5*i6*i7
                            if(pr>limit**0.5):
                                break
                            s7 += limit//(pr**2)
print("s7 done")

for i1 in primes:
    for i2 in [p for p in primes if p>i1]:
        if(i1*i2>limit**0.5):
            break
        for i3 in [p for p in primes if p>i2]:
            if(i1*i2*i3>limit**0.5):
                break
            for i4 in [p for p in primes if p>i3]:
                if(i1*i2*i3*i4>limit**0.5):
                    break
                for i5 in [p for p in primes if p>i4]:
                    if(i1*i2*i3*i4*i5>limit**0.5):
                        break
                    for i6 in [p for p in primes if p>i5]:
                        if(i1*i2*i3*i4*i5*i6>limit**0.5):
                            break
                        for i7 in [p for p in primes if p>i6]:
                            if(i1*i2*i3*i4*i5*i6*i7>limit**0.5):
                                break
                            for i8 in [p for p in primes if p>i7]:
                                pr = i1*i2*i3*i4*i5*i6*i7*i8
                                if(pr>limit**0.5):
                                    break
                                s8 += limit//(pr**2)
print("s8 done")

for i1 in primes:
    for i2 in [p for p in primes if p>i1]:
        if(i1*i2>limit**0.5):
            break
        for i3 in [p for p in primes if p>i2]:
            if(i1*i2*i3>limit**0.5):
                break
            for i4 in [p for p in primes if p>i3]:
                if(i1*i2*i3*i4>limit**0.5):
                    break
                for i5 in [p for p in primes if p>i4]:
                    if(i1*i2*i3*i4*i5>limit**0.5):
                        break
                    for i6 in [p for p in primes if p>i5]:
                        if(i1*i2*i3*i4*i5*i6>limit**0.5):
                            break
                        for i7 in [p for p in primes if p>i6]:
                            if(i1*i2*i3*i4*i5*i6*i7>limit**0.5):
                                break
                            for i8 in [p for p in primes if p>i7]:
                                if(i1*i2*i3*i4*i5*i6*i7*i8>limit**0.5):
                                    break
                                for i9 in [p for p in primes if p>i8]:
                                    pr = i1*i2*i3*i4*i5*i6*i7*i8*i9
                                    if(pr>limit**0.5):
                                        break
                                    s9 += limit//(pr**2)
print("s9 done")                           
print(2**50-s1+s2-s3+s4-s5+s6-s7+s8-s9)