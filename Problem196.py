# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 17:33:11 2021

@author: Tobi
"""

"""
Problem 196:
Build a triangle from all positive integers in the following way:

 1
 2  3
 4  5  6
 7  8  9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
. . .

Each positive integer has up to eight neighbours in the triangle.
A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours in the triangle.
For example, in the second row, the prime numbers 2 and 3 are elements of some prime triplet.
If row 8 is considered, it contains two primes which are elements of some prime triplet, i.e. 29 and 31.
If row 9 is considered, it contains only one prime which is an element of some prime triplet: 37

Define S(n) as the sum of the primes in row n which are elements of any prime triplet.
Then S(8)=60 and S(9)=37

You are given that S(10000)=950007619

Find S(5678027) + S(7208785)

Solution:
First, we have to find S(5678027) and S(7208785), for that, we have to know which numbers are in row 5678025, 5678026, 5678027, 5678028, 5678029 and
7208783, 7208784, 7208785, 7208786, 7208787. One can find with the Gaussian sum which numbers are in a row. That is, there are numbers n(n-1)/2+1 until n(n+1)/2 in row n

"""

# Generate primes <= sqrt of largest number that has to be tested
def primes(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3,int(1 + n**0.5),2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r

largest_num_to_check = int(7208785*(7208785+1)/2)

prime_list = primes(int(largest_num_to_check**0.5)+1)
prime_list = [i for i,x in enumerate(prime_list) if x]

# helper function which calculates all triplets which have the middle prime in row n
def calc_triplets_of_row(n, dic):
    ls = []
    for i,x in [(i,x) for i,x in enumerate(dic[n]) if x>0]:
        a11, a12, a13, a31, a32, a33 = 0,0,0,0,0,0
        if i-1>=0 and i-1<len(dic[n-1]):
            a11 = dic[n-1][i-1]
        if i<len(dic[n-1]):
            a12 = dic[n-1][i]
        if i+1<len(dic[n-1]):
            a13 = dic[n-1][i+1]
        if i-1>=0 and i-1<len(dic[n+1]):
            a31 = dic[n+1][i-1]
        if i<len(dic[n+1]):
            a32 = dic[n+1][i]
        if i<len(dic[n+1]):
            a33 = dic[n+1][i+1]
        window = [a11, a12, a13, x, a31, a32, a33]
        window = [a for a in window if a>0]
        if len(window)>2:
            ls.append(window)
    return(ls)

# calculate S. For that the primes two rows above and below the relevant row have to be determined
# such that the triplets which have their middle prime in rows n-1, n, or n+1 can be calculated
def calc_S(S):    
    Ss = [S-2, S-1, S, S+1, S+2]
    dic = {}
    for n in Ss:
        dic[n] = list(range(int(n*(n-1)/2)+1, int(n*(n+1)/2)+1))
    
    for n in Ss:
        start = int((n-1)*n/2)+1
        for p in prime_list:
            dic[n][(p-(start%p))%p::p] = len(dic[n][(p-(start%p))%p::p])*[0]
    
    triplets = calc_triplets_of_row(S-1, dic) + calc_triplets_of_row(S, dic) + calc_triplets_of_row(S+1, dic)
    
    triplet_primes_all_rows = sum(triplets, [])
    
    res = list(set(triplet_primes_all_rows).intersection(set([x for x in dic[S] if x>0])))
    return(sum(res))

from time import time
start = time()
print(calc_S(5678027) + calc_S(7208785))
end = time()
print("solved in ", end-start, " seconds")

# 322303240771079935
# solved in  46.52362060546875  seconds