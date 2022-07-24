# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 13:27:06 2021

@author: Tobi
"""

# Generate primes
def primes(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3,int(1 + n**0.5),2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r

prime_list = primes(4*10**7)
prime_list = [i for i,x in enumerate(prime_list) if x]

def prime_factorization(n):
    #if n in prime_list:
        #return [n]
    primfac = []
    p = 2
    d = 0
    while p*p <= n:
        while (n % p) == 0:
            primfac.append(p)  # supposing you want multiple factors repeated
            n //= p
        d += 1
        p = prime_list[d]
    if n > 1:
       primfac.append(n)
    return primfac

all_prime_factorizations = {}
for i in prime_list:
    i = i-1
    if i%10**5==0:
        print(i)
    if i in prime_list:
        all_prime_factorizations[i] = [i]
    else:
        all_prime_factorizations[i] = prime_factors(i)


prime_list[-1] # 39999983

prime_factors(39999982)

def phi(n):
    prime_factors = prime_factorization(n)
    factors_unq = list(set(prime_factors))
    phi = 1
    for p in factors_unq:
        e = prime_factors.count(p)
        phi *= (p-1) * p**(e-1)
    return phi

# Vorüberlegung: Die kleinste Zahl, für die phi^25(n) = 1 und phi^i(n) > 1 für i=1,...,24 ist, muss
# ziemlich groß sein, da die phi funktion, die Zahlen schnell schrumpfen lässt. Wie lange ist also
# die längste Kette für alle Zahlen <= 10**6?
phis = {}
for i in range(1,10**6):
    if i%10**6==0:
        print(i)
    phis[i] = phi(i)
   
chain = {}
for p in phis.keys():
    i=1
    s = p
    while s>1:
        s = phis[s]
        i += 1
        chain[p] = i
        
max(chain.values()) #21
# --> wenn man die ketten mal für alle zahlen bis 10**6 laufen lässt, sieht man, dass die längste kette 21
# lang ist. Also, brauch man die Primzahlen <10**6 gar nicht checken

        
len([p for p in prime_list if p>10**6]) # 2,355,156
# --> ok, das könnte runtime technisch sinn ergeben.

# iteriere über all diese Primzahlen, man kann bei 3 anfangen, denn das erste Kettenglied ist p selbst,
# phi(p)=p-1, also ist das erste Glied, das man ausrechnen muss, das dritte Kettenglied, also phi^2(p)
# =phi(p-1). Den rest kann man durchiterieren, bis man bei 1 landet. Alle Primzahlen, deren Ketten
# schon früher bei 1 landen, kann man auf 0 setzen.
def iterate_phis(large_primes):
    i = 3
    phis = {}
    for p in large_primes:
        phis[p] = phi(p-1)
    while i<=24:
        print(i)
        for k,v in [(k,v) for k,v in phis.items() if v>1]:
            ph = phi(v)
            phis[k] = ph
            if ph==1 and i<24:
                phis[k] = 0
        i += 1
    return phis

res = iterate_phis([a for a in prime_list if a >= 10**6])

sum([k for k,v in res.items() if v==1]) # 1677366278943

# Just for fun
len([k for k,v in res.items() if v==1]) # 51147 --> interessant, sind recht viele Primzahlen

len([(k,v) for k,v in res.items() if v>1]) # 1870 --> und 1870 haben sogar noch längere Ketten

len([(k,v) for k,v in res.items() if v>2]) # 2 --> aber nur 2 haben noch längere Ketten

[(k,v) for k,v in res.items() if v>2]
# [(35946497, 4), (37880387, 4)]