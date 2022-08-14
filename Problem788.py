# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 16:09:06 2022

@author: Tobi
"""

from sqlalchemy import Boolean
from scipy.special import binom


mod_const = 10**9+7
pot_dict = dict({0: 1, 1: 9})
binom_dict = dict()
end = 2022
for i in range(2,2022):
    pot_dict[i] = 9*pot_dict[i-1] % mod_const
 
for i in range(1,end+1):
    binom_dict[(i,0)] = 1
    binom_dict[(i,i)] = 1
    for j in range(1,i):
        binom_dict[(i,j)] = (binom_dict[(i-1,j-1)] + binom_dict[(i-1,j)]) % mod_const
            
cnt = 0
for i in range(1,end+1):
    if i%2==0:
        start_j = int(i/2+1)
    else:
        start_j = int(i/2)+1
    for j in range(start_j, i+1):
        cnt += 9*pot_dict[(i-j)] % (mod_const) * binom_dict[(i,j)] % (mod_const)
        cnt %= (mod_const)
print(cnt) # 471745499