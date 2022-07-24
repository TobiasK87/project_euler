# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 00:23:22 2017

@author: Tobi
"""

import numpy as np

text_file = open(r"C:\Users\Tobi\Documents\Python Scripts\EulerProject\p099_base_exp.txt", "r")
lines = text_file.read()
temp = lines.splitlines()
#temp.split(',')
text_file.close()

lst=[]
for i in range(0,len(temp)):
    spl = temp[i].split(',')
    lst.extend(spl)
    
largest = float(lst[1]) * np.math.log(float(lst[0]))
for i in range(0,int(len(lst) / 2)):
    a = float(lst[2*i +1 ]) * np.math.log(float(lst[2*i]))
    if a > largest:
        largest_idx = i
        largest = a

print(largest_idx+1) # Python fängt bei 0 an zu zählen, die Frage war aber nach der Zeilennummer
print(largest)