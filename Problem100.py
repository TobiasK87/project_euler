# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 15:06:09 2019

@author: Tobi
"""

def update(b,n):
    b_new = 3*b+2*n-2
    n_new = 4*b+3*n-3
    return b_new,n_new

b,n,b_new,n_new=1,1,1,1

i=0
while True:
    b,n=b_new,n_new
    b_new,n_new=update(b,n)
    # print(b_new,n_new)
    i+=1
    if n_new>10**12:
        break

print(b_new)
update(1,1)
183648021600>10**12

# see 

# für n=10**7, b=19306983, 27304197

print(prime_factors(b))
print(prime_factors(n))
print(prime_factors(b-1))
print(prime_factors(n-1))

for pair in ls:
    print(prime_factors(pair[0]))
    print(prime_factors(pair[0]-1))
    print(prime_factors(pair[1]))
    print(prime_factors(pair[1]-1))
    

        
c = np.sqrt(2)/2
c*10**12  # 707106781186.54761

c*21
c*20

15/21>c
14/20<c
print(c*24)
print(c*23)
print(17/24>c)
print(16/23<c)

import math

n=1000000030324+1
while True:
    b=math.ceil(c*n)
    if b*(b-1)/(n*(n-1))==0.5:
        print(b,n)
        break
    n+=1
    
    
    
    
###### COPY
    # COULD WORK BUT TAKES TOO LONG
# b_lower = 707106781187
b_lower=1
n=10**7
b=b_lower
while True:
    if b%10**6==0:
        print(n)
    while True:
        prod = int(n*(n-1))
        f=func(b)
        if prod<f:
            n+=1
        if prod>f:
            break
        if prod==f:
            print(b, n)
            break
    if prod==f:
        break
    b+=1