""" EULER PROBLEM 816: https://projecteuler.net/problem=816
We create an array of points  P_n in a two dimensional plane using the following random number generator:
s_0=290797
s_{n+1}={s_n}^2 mod 50515093
P_n=(s_{2n},s_{2n+1})

Let d(k) be the shortest distance of any two (distinct) points among P_0, ..., P_{k - 1}.
E.g. d(14)=546446.466846479.

Find d(2000000). Give your answer rounded to 9 places after the decimal point.

===================================================================================================================

Solution:

Idea: This is the classical https://en.wikipedia.org/wiki/Closest_pair_of_points_problem to be solved in O(n*log(n)) time by divide and conquer

"""

def create_coordinates(n):
    s = [290797]
    for i in range(n):
        s.append(s[-1]**2%50515093)
    return s

def create_points(n):
    s = create_coordinates(2*n)
    p = []
    for i in range(2*n)[::2]:
        p.append((s[i], s[i+1]))
    return p

# main part
def ccp(ps: list):
    size = len(ps)
    if size <= 3:
        d = brute_force(ps)
        return d

    ps.sort(key=lambda x: x[0])
    if size%2==0:
        mid = int(size/2)
        median = (ps[int(size/2-1)][0] + ps[int(size/2)][0])/2
    else:
        mid = int((size-1)/2)+1
        median = ps[int((size-1)/2)][0]
    left = ps[:mid]
    right = ps[mid:]
    d_left = ccp(left)
    d_right = ccp(right)
    d = min(d_left, d_right)
    ps_mid = [p for p in ps if abs(p[0] - median) <= d]
    ps_mid.sort(key=lambda x: x[1])
    d_mid = brute_force(ps_mid, mid=True)
    d = min(d, d_mid)
    return d

def brute_force(ps: list, mid: bool = False):
    min_dist = 10**10
    for i,p in enumerate(ps):
        for j, q in enumerate(ps):
            if i==j:
                continue
            if i>j:
                break
            if mid and j>i+7:
                break
            d = eucl_dist(p,q)
            if d < min_dist:
                min_dist = d
    return min_dist
            

def eucl_dist(p, q):
    return ((p[0]-q[0])**2 + (p[1]-q[1])**2)**0.5

n = 2*10**6
# n = 14

points = create_points(n)
res = ccp(points)
print(round(res, 9)) # 20.880613018