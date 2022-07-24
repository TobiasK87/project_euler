stri# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:34:13 2019

@author: Tobi
"""

## KORREKTER CODE IST GANZ UNTEN

a = str(int(np.sqrt(2)*10**50))
cnt=0
for i in range(len(str(int(np.sqrt(2)*10**50)))):
    #print(a[i])
    cnt+=int(a[i])
print(cnt)
    
def ggT(a,b):
    if a==0:
        return abs(b)
    if b==0:
        return abs(a)
    while True:
        h=a%b
        a=b
        b=h
        if b==0:
            break
    return abs(a)

def newton(a,x_n):
    return x_n/2*(3-x_n**2/a)
x_n = 1
x_n = newton(2,x_n)
print(x_n)

print(newton(2,1.4142135623726146))

def newton(a,p_n,q_n):
    p_nplus1 = 3*a*p_n*q_n**2-p_n**3
    q_nplus1 = 2*a*q_n**3
    return int(p_nplus1/ggT(p_nplus1,q_nplus1)), int(q_nplus1/ggT(p_nplus1,q_nplus1))

def newton2(a,p_n,q_n):
    p_nplus1 = 3*a*p_n*q_n**2-p_n**3
    q_nplus1 = 2*a*q_n**3
    return int(p_nplus1), int(q_nplus1)


p=1
q=1
while True:
    p_old=p
    p,q=newton(a,p,q)
    if p==p_old:
        break
p,q=newton2(a,p,q)
p,q=newton2(a,p,q)    

length=101
stri=0
p_new=p
for i in range(length):
    digit = p_new//q
    p_new = (p_new%q)*10
    stri += digit
print(stri)


import numpy as np
np.sqrt(2)-int(p/q*10**100)


cnt=0
for i in range(106):
    cnt+=int(str(int(p/q*10**105))[i])
print(cnt)

a=2
p=1
q=1
while True:
    p,q=newton2(a,p,q)
    if len(str(p))>400:
        break




ggT(p,q)

p//q
(p%q)*10//q

def digits(p,q,length):
    p_new=p
    stri = ""
    for i in range(length):
        digit = p_new//q
        p_new = (p_new%q)*10
        stri = stri + str(digit)
    return stri

digits(p,q,100)
print(digits(p,q,10))






#########
nonsquares = sorted(list(set(list(range(2,100)))-set([i**2 for i in range(2,10)])))
print(nonsquares)
cnt=0
for a in nonsquares:
    p=1
    q=1
    i=0
    while True:
        if i>5000:
            break
        p_old=p
        p,q=newton(a,p,q)
        i+=1
        if p==p_old or len(str(p))>10000:
            break
    i=0
    while True:
        if i>10:
            break
        p_old=p
        p,q=newton2(a,p,q)
        i+=1
    
    length=101
    stri=0
    p_new=p
    for i in range(length):
        digit = p_new//q
        p_new = (p_new%q)*10
        stri += digit
    print(a, stri)
    cnt+=stri
print(cnt)



### COPY
a=3
p=1
q=1
while True:
    p_old=p
    p,q=newton(a,p,q)
    if p==p_old:
        break
p,q=newton2(a,p,q)
p,q=newton2(a,p,q)    

length=101
stri=0
p_new=p
for i in range(length):
    digit = p_new//q
    p_new = (p_new%q)*10
    stri += digit
print(stri)



### COPY

a=2
p=1
q=1
i=0
while True:
    if i>100:
        break
    i+=1
    p_old=p
    p,q=newton2(a,p,q)
    if p==p_old:
        break
# p,q=newton2(a,p,q)
# p,q=newton2(a,p,q)    

length=101
stri=0
p_new=p
for i in range(length):
    digit = p_new//q
    p_new = (p_new%q)*10
    stri += digit
print(stri)




##### KORRECTER CODE

from decimal import *

nonsquares = sorted(list(set(list(range(2,100)))-set([i**2 for i in range(2,10)])))
getcontext().prec = 103
cnt=0
for s in nonsquares:
    a = Decimal(s).sqrt()*10**103
    a_str = str(a)
    a_str = a_str.replace('.','')
    stri=0
    for i in range(100):
        digit = int(a_str[i])
        stri += digit
    print(s, stri)
    cnt+=stri
print(cnt) # 40886