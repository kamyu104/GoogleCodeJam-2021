# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem D. Binary Search Game
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813e1b
#
# Time:  O(N * 2^(2^(L-1)) * 2^L), pass in PyPy2 but Python2
# Space: O(N + L)
#
# optimized from binary_search_game.py, less time and space complexity, faster in power function,
# but slower in recursive check function (iterative one is even slower since 2^L is small) compared to dp,
# so overall runtime is slower
#

from collections import Counter

def addmod(a, b):
    return (a+b)%MOD
        
def mulmod(a, b):
    return (a*b)%MOD

def inverse(n):  # compute and cache, at most O(N) time and O(N) space in all test cases
    while len(inv) <= n:  # lazy initialization
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
    return inv[n]

def inverse_factorial(n):  # compute and cache, at most O(N) time and O(N) space in all test cases
    while len(inv_fact) <= n:  # lazy initialization
        inv_fact.append(inv_fact[-1]*inverse(len(inv_fact)) % MOD)
    return inv_fact[n]

# f(x) = c(N+1)*x^(N+1) + c(N)*x^N + ... + c(0)*x^0
# given f(0), f(1), ... f(N+1), compute f(M)
# usually, this should be done in O(N^2) time,
# since x0, x1, ..., x(n-1) are consecutive integers,
# we can compute in O(N) time
def lagrange_interpolation(f, x):  # Time: O(N)
    n = len(f)
    prefix = [1]*n
    for i in xrange(1, len(f)):  # (x-x0)*(x-x1)* ... * (x-x(n-1))
        prefix[i] = mulmod(prefix[i-1], x-(i-1))
    suffix = [1]*n
    for i in reversed(xrange(len(f)-1)):
        suffix[i] = mulmod(suffix[i+1], x-(i+1))
    result = 0
    for i in xrange(len(f)):
        a = mulmod(prefix[i], suffix[i])  # (x-x0)*(x-x1)* ... * (x-x(n-1)) / (x-xi)
        b = mulmod(inverse_factorial(i), mulmod((-1)**((n-1-i)%2), inverse_factorial(n-1-i)))  # (1/i!) * ((-1)^((n-1-i)%2)/(n-1-i)!)
        result = addmod(result, mulmod(f[i], mulmod(a, b)))
    return result

def mask_to_set(R, mask): # Time: O(N)
    result = set()
    for i in R:
        if mask&1:
            result.add(i)
        mask >>= 1
    return result

def check(A, values, left, right):  # Time: O(2^L), Space: O(L)
    if left == right:
        return values[A[left]]
    mid = left + (right-left)//2
    win1, lose1 = check(A, values, left, mid)
    win2, lose2 = check(A, values, mid+1, right)
    return [addmod(addmod(mulmod(lose1, lose2),
                          mulmod(lose1, win2)),
                          mulmod(win1, lose2)),
            mulmod(win1, win2)]

# given chosen subset C from R where card values are all >= k,
# count the number of ways to get final score >= k by considering the card values of U
def count(N, M, L, A, U, R, C, k):  # Time: O(2^L), Space: O(N + L)
    g = max(min(M-(k-1), M), 0)  # number of choices greater or equal to k
    l = max(min(k-1, M), 0)  # number of choices less than k
    # last decision done by whom would affect initial dp
    values = {i:[l, g] if i in U else [0, 1] if i in C else [1, 0] for i in set.union(U, R)} if L%2 else \
             {i:[g, l] if i in U else [1, 0] if i in C else [0, 1] for i in set.union(U, R)}
    return mulmod(mulmod(check(A, values, 0, len(A)-1)[0],
                         pow(g, len(C), MOD)),
                         pow(l, N-len(U)-len(C), MOD))  # since pow(x, N, MOD) is O(logN), and N <= 32, we treat it as O(1)

def binary_search_game():
    N, M, L = map(int, raw_input().strip().split())
    A = map(lambda x : int(x)-1, raw_input().strip().split())

    cnt = Counter(A)
    U, R = set(), set()  # unique set and repeated set
    for i in A:
        if cnt[i] == 1:
            U.add(i)
        else:
            R.add(i)
    Z = set(i for i in xrange(N) if i not in U and i not in R)  # unused set
    N -= len(Z)
    assert(len(R) <= len(A)//2)
    # f(x) which means the number of ways where the final scores is >= x, is a polynomial of x with at most N-degree
    # accumulated f(x) which means the sum of final scores with x^N different games, is a polynomial of x with at most (N+1)-degree by Faulhaber's formula,
    # and could be determinated by N+2 values of accumulated f(x)
    f = [0]*(min(N+1, M)+1)  # if M < N+1, we can also just loop until f[M] is computed
    for mask in xrange(2**len(R)):  # O(2^(2^(L-1))) times
        C = mask_to_set(R, mask)
        for k in xrange(1, len(f)):  # O(N) times
            f[k] = addmod(f[k], count(N, M, L, A, U, R, C, k))  # Time: O(2^L)
    for k in xrange(1, len(f)):
        f[k] = addmod(f[k], f[k-1])  # accumulate f
    return mulmod(lagrange_interpolation(f, M), pow(M, len(Z), MOD))  # Time: O(N), since pow(x, N, MOD) is O(logN), and N <= 32, we treat it as O(1)

MOD = 10**9+7
inv = [0, 1]
inv_fact = [1, 1]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_search_game())
