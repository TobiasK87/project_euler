# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 12:50:13 2021

@author: Tobi
"""

l = []
ls = []
# num = int(input("Enter a number: "))
num = 12

def findCombinations(n, product):
    global l, ls
    
    #Base condition
    if product == num:
        # print(l)
        ls.append(l.copy())
        return(l)

    for x in range(n, int(num/2)+1):
        #If product exceeds num -> return to last recursive call
        if product*x > num:
            return(ls)
        
        #Add number to product i.e. multiply    
        product = product * x
        l.append(x)
        
        #Recursive call with same number
        # print("(x, product, ",x, product)
        findCombinations(x, product)

        #Backtrack
        l.pop()
        product = product//x
       
    # print("ganz unten", l)
    return(ls)

A = findCombinations(2,1)
A