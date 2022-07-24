# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 21:52:12 2017

@author: Tobi
"""

text_file = open(r"C:\Users\Tobi\Documents\Python Scripts\EulerProject\p042_words.txt", "r")
lines = text_file.read()
temp = lines.splitlines()
temp = lines.split(',')
text_file.close()


gauss = [p*(p+1)/2 for p in range(1,101)]

ls = []
dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
for i in range(len(temp)):
    word = temp[i]
    l = 0
    for j in range(1,len(word)-1):
        char = word[j]
        l += dic[char]
    if l in gauss:
        ls.extend([l])
    
ls
len(ls) # 162