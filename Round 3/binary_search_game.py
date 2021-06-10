# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem D. Binary Search Game
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813e1b
#
# Time:  O(N * 2^(2^(L-1)) * 2^L), pass in PyPy2 but Python2
# Space: O(N + 2^L)
#

from collections import Counter, defaultdict

def addmod(a, b):
    return (a+b)%MOD
        
def mulmod(a, b):
    return (a*b)%MOD

def inverse(n):
    while len(inv) <= n:  # lazy initialization
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
    return inv[n]

def inverse_factorial(n):  # lazy initialization
    while len(inv_fact) <= n:  # lazy initialization
        inv_fact.append(inv_fact[-1]*inverse(len(inv_fact)) % MOD)
    return inv_fact[n]

def power(x, y):
    while len(POW[x]) < y+1:
        POW[x].append(mulmod(POW[x][-1], x))
    return POW[x][y]

# f(x) = c(n+1)*x^(n+1) + c(n)*x^n + ... + c(0)*x^0
# given f(0), f(1), ... f(N+1),
# compute f(M)
def lagranges_interpolation(f, x):  # Time: O(N)
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
        b = mulmod(inverse_factorial(i), mulmod((-1)**((n-1-i)%2), inverse_factorial(n-1-i)))  # 1 / i! * ((-1)^((n-1-i)%2) / (n-1-i)!)
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

def count(N, M, L, A, U, R, k, mask):
    selected = decode_mask(R, mask)
    a = max(min(M-k+1, M), 0)
    b = max(k-1, 0)
    dp = [[a, b][::-1 if L%2 else 1] if i in U else \
          ([1, 0][::-1 if L%2 else 1] if i in selected else \
           [0, 1][::-1 if L%2 else 1]) for i in A]
    while len(dp) != 1:
        dp = [[addmod(addmod(mulmod(dp[2*i][1], dp[2*i+1][1]),
                             mulmod(dp[2*i][1], dp[2*i+1][0])),
                             mulmod(dp[2*i][0], dp[2*i+1][1])),
               mulmod(dp[2*i][0], dp[2*i+1][0])]
              for i in xrange(len(dp)//2)]
    result = dp[0][0]
    result = mulmod(result, power(a, len(selected)))
    result = mulmod(result, power(b, N-len(U)-len(selected)))
    return result

def binary_search_game():
    N, M, L = map(int, raw_input().strip().split())
    A = map(lambda x : int(x)-1, raw_input().strip().split())

    cnt = Counter(A)
    U, R = set(), set()
    for i in A:
        if cnt[i] == 1:
            U.add(i)
        else:
            R.add(i)
    Z = set(i for i in xrange(N) if i not in U and i not in R)
    N -= len(Z)
    R = list(R)
    assert(len(R) <= len(A)//2)
    f = [0]*(N+2)
    for k in xrange(1, len(f)):  # O(N) times
        for mask in xrange(2**len(R)):  # O(2^(2^(L-1))) times
            f[k] = addmod(f[k], count(N, M, L, A, U, R, k, mask))  # Time: O(2^L)
    for i in xrange(1, len(f)):  # accumulate f, Time: O(N)
        f[i] += f[i-1]
    return mulmod(lagranges_interpolation(f, M), power(M, len(Z)))  # Time: O(N)

MOD = 10**9+7
inv = [0, 1]
inv_fact = [1, 1]
POW = defaultdict(lambda:[1])
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_search_game())
