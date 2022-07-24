# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 17:50:46 2017

@author: Tobi
"""

def mult_10(a,n):
    i = -1
    while a/n < 1:
        a *= 10
        i += 1
    return a,i

# berechnet 1/n bis es periodisch wird
def schriftliche_division(n):
    rest, nullen = mult_10(1,n)
    bruch = str(0) + '.' + nullen * str(0)
    dic = {rest: nullen}
    period = 0
    nullen = 0
    i = 0        
    while True:
        i = i + 1 + nullen
        digit = rest // n
        rest = rest % n
        if rest in dic:
            period = i - dic[rest]
            break
        bruch = bruch + nullen * str(0) + str(digit)
        temp_dic = {rest: i}
        dic.update(temp_dic)
        if rest % n == 0:
            period = i
            break
        rest, nullen = mult_10(rest,n)
    return(bruch, period)

print(schriftliche_division(997)[1])
    
longest_period = 0    
for i in range(2,1001):
    period = schriftliche_division(i)[1]
    if period > longest_period:
        nenner = i
        longest_period = int(period)

print(nenner) # 983
print(longest_period) # 982