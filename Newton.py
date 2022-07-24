# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:34:13 2019

@author: Tobi
"""

a = str(int(np.sqrt(2)*10**50))
cnt=0
for i in range(len(str(int(np.sqrt(2)*10**50)))):
    #print(a[i])
    cnt+=int(a[i])
print(cnt)


def newton(a,x_n):
    return x_n/2*(3-x_n**2/a)
x_n = 1
x_n = newton(2,x_n)
print(x_n)

print(newton(2,1.4142135623726146))

def newton(a,p_n,q_n):
    p_nplus1 = 3*a*p_n*q_n**2-p_n**3
    q_nplus1 = 2*a*q_n**3
    return p_nplus1, q_nplus1

p=1
q=1
p,q=newton(2,p,q)
print(p,q)

p//q
(p%q)*10//q

def digits(p,q,length):
    p_new=p
    q_new=q
    stri = ""
    for i in range(length):
        