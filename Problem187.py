# TODO: Optimize runtime, take more than 10 minutes


limit = 10**8
#limit = 30

def primes(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3,int(1 + n**0.5),2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r
prime_list = primes(int(limit/2))

pi = dict()
prime_list_true = []
cnt = 0
for idx,i in enumerate(prime_list):
    if idx%10**6==0:
        print(idx, i)
    if i:
        cnt+=1
        prime_list_true.append(idx)
    pi[idx] = cnt
pi[idx+1]=cnt

# prime_list = [i for i,x in enumerate(prime_list) if x]

"""
smaller_equal_primes = [1]
larger_equal_primes = [2,2]
for last_prime, current_prime in zip(prime_list[:-1], prime_list[1:]):
     smaller_equal_primes.extend((current_prime-last_prime)*[last_prime])

dic = dict([(v,k+1) for (k,v) in enumerate(prime_list)])
pi = dict([(i+2,dic[x]) for (i,x) in enumerate(smaller_equal_primes[1:])])
"""


# seperate treatment for primes < 100
cnt=0
"""
sub = 0
for i in prime_list_true[:25]:
    new = sum(prime_list[::i])
    cnt+= new-sub
    sub = new
"""



for i,p in enumerate(prime_list_true):
    if p**2>=limit:
        break
    if i%100000==0:
        print(i,p)
    if p==2:
        cnt+=pi[limit//p]
    else:
        cnt+=pi[limit//p]-pi[p-1]

print(cnt) # 17427258

# not 3001134
# not 34853287
# not 5710617