# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 19:04:21 2021

@author: Tobi
"""

### mach es mit Pentagonalzahlen, da besteht eine Rekursionsformel bzw. ein Zusammenhang, siehe
# https://de.wikipedia.org/wiki/Pentagonalzahlensatz

from math import pow

dic = {0:1, 1:1, 2:2}

def pent(k):
    return(int((3*k**2-k)/2))

def calc_p(n):
    k = 1
    p = 0
    while True:
        gk = pent(k)
        if n-gk<0:
            break
        p_of_gk_from_dic = dic.get(n-gk, 0)
        if k==1:
            if p_of_gk_from_dic!=0:
                p += p_of_gk_from_dic
            else:
                p += calc_p(n-gk)
        else:
            if p_of_gk_from_dic!=0:
                p += (int(pow(-1,k-1)))*p_of_gk_from_dic
            else:
                p += (int(pow(-1,k-1)))*calc_p(n-gk)
        k += 1
    k = 1
    while True:
        g_minus_k = pent(-k)
        if n-g_minus_k<0:
            break
        p_of_g_minus_k_from_dic = dic.get(n-g_minus_k, 0)
        if p_of_g_minus_k_from_dic!=0:
            p += (int(pow(-1,-k-1)))*p_of_g_minus_k_from_dic
        else:
            p += (int(pow(-1,-k-1)))*calc_p(n-g_minus_k)
        k += 1
    dic[n] = p
    return(p)

i = 4
while True:
    if i%10**4==0:
        print(i)
    if calc_p(i)%10**6==0:
        print(i)
        break
    i+=1
    
# 55374
calc_p(55374)