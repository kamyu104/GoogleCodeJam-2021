# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem D. Binary Search Game
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813e1b
#
# Time:  O(N^2 + N * 2^(2^(L-1)) * 2^L), pass in PyPy2 but Python2
# Space: O(N^2 + 2^L)
#

from collections import defaultdict, Counter

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

def power(x, y):  # compute and cache, at most O(N^2) time and O(N^2) space in each test case
    while len(POW[0][x]) <= y:  # lazy initialization
        POW[0][x].append(mulmod(POW[0][x][-1], x))
    return POW[0][x][y]

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

def decode_mask(R, mask):
    result = set()
    i = 0
    while mask:
        if mask&1:
            result.add(R[i])
        i += 1
        mask >>= 1
    return result

def count(N, M, L, A, U, C, k):
    g = max(min(M-(k-1), M), 0)  # number of choices greater or equal to k
    l = max(min(k-1, M), 0)  # number of choices less than k
    # last decision done by whom would affect initial dp
    dp = [[l, g] if i in U else [0, 1] if i in C else [1, 0] for i in A] if L%2 else \
         [[g, l] if i in U else [1, 0] if i in C else [0, 1] for i in A]
    while len(dp) != 1:
        dp = [[addmod(addmod(mulmod(dp[2*i][1], dp[2*i+1][1]),
                             mulmod(dp[2*i][1], dp[2*i+1][0])),
                             mulmod(dp[2*i][0], dp[2*i+1][1])),
               mulmod(dp[2*i][0], dp[2*i+1][0])]
              for i in xrange(len(dp)//2)]
    return mulmod(mulmod(dp[0][0],
                         power(g, len(C))),
                         power(l, N-len(U)-len(C)))

def binary_search_game():
    N, M, L = map(int, raw_input().strip().split())
    A = map(lambda x : int(x)-1, raw_input().strip().split())

    POW[0] = defaultdict(lambda:[1])  # cleanup global used cache to save space
    cnt = Counter(A)
    U, R = set(), set()  # unique set and repeated set
    for i in A:
        if cnt[i] == 1:
            U.add(i)
        else:
            R.add(i)
    Z = set(i for i in xrange(N) if i not in U and i not in R)  # unused set
    N -= len(Z)
    R = list(R)
    assert(len(R) <= len(A)//2)
    f = [0]*(N+2)  # f(x) is a polynomial of x with at most N-degree, thus accumulated f(x) is a polynomial of x with at most (N+1)-degree by Faulhaber's formula, which could be determinated by N+2 values of f(x)
    for k in xrange(1, min(len(f), M+1)):  # O(N) times, we can also early break if M < N+1
        for mask in xrange(2**len(R)):  # O(2^(2^(L-1))) times
            f[k] = addmod(f[k], count(N, M, L, A, U, decode_mask(R, mask), k))  # Time: O(2^L)
        f[k] += f[k-1]  # accumulate f
    return mulmod(lagrange_interpolation(f, M), power(M, len(Z)))  # Time: O(N)

MOD = 10**9+7
inv = [0, 1]
inv_fact = [1, 1]
POW = [None]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_search_game())
