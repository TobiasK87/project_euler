# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 07:47:02 2019

@author: Tobi
"""

while cnt<4*10**6:
    
    cnt = 0
    r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16 = [11,9,5,5,3,3,3,3,3,3,3,3,3,3,3,3]
    n = 2**((r1-1)/2) * 3**((r2-1)/2) * 5**((r3-1)/2) * 7**((r4-1)/2) * 11**((r5-1)/2) * 13**((r6-1)/2) * 17**((r7-1)/2) * 19**((r8-1)/2) * 23**((r9-1)/2) * 29**((r10-1)/2) * 31**((r11-1)/2) * 37**((r12-1)/2) * 41**((r13-1)/2) * 43**((r14-1)/2) * 47**((r15-1)/2) * 53**((r16-1)/2)
    for e1 in range(r1):
        for e2 in range(r2):
            for e3 in range(r3):
                for e4 in range(r4):
                    for e5 in range(r5):
                        for e6 in range(r6):
                            for e7 in range(r7):
                                for e8 in range(r8):
                                    for e9 in range(r9):
                                        for e10 in range(r10):
                                            for e11 in range(r11):
                                                for e12 in range(r12):
                                                    for e13 in range(13):
                                                        for e14 in range(14):
                                                            for e15 in range(15):
                                                                for e16 in range(16):
                                                                    if 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11 * 37**e12 * 41**e13 * 43**e14 * 47**e15 * 53**e16<= n:
                                                                        cnt +=1
                                                                        if cnt%10**5==0:
                                                                            print(cnt)
print(cnt)