# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def abundance_check(n):
    s = 0
    abundant = 0
    for i in range(1,int(n/2+1)):
        if n%i==0:
            s += i
    if s > n:
        abundant = 1
    return abundant
    
abundance_list = []
for i in range(12,28124):
    if abundance_check(i)==1:
        abundance_list.extend([i])
        
abundance_sum = set([])
for i in abundance_list:
#    J = list(set(range(1,28123-i)) & set(abundance_list))
    J = abundance_list
    for j in J:
        s = i + j
        if s > 28123: # 28123 is grenze, danach ist jede Zahl als Summe zweier abundanter Zahlen darstellbar
            break
        abundance_sum.update({s})

M = sorted(list(set(range(1,28124)) - set(abundance_sum)))
print(sum(list(M))) # 4179871
