from collections import Counter

p_limit = 5*10**7

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def primes(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3,int(1 + n**0.5),2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r
prime_list = [i for i,x in enumerate(primes(p_limit)) if x]

prime_squares = [p**2 for p in prime_list]
prime_squares_reverse = [int(str(p)[::-1]) for p in prime_squares if not is_palindrome(p)]

x = set(prime_squares).intersection(set(prime_squares_reverse))
y = list(x)
y.sort()
len(y) # 50
print(sum(y[:50])) # 3807504276997394
