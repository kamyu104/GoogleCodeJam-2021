# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem D. Binary Search Game
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813e1b
#
# Time:  O(2^(2^(L-1)) * (2^L + N^2) + N^3)
# Space: O(N^2 + L)
#

from collections import Counter

def addmod(a, b):
    return (a+b)%MOD

def submod(a, b):
    return (a-b)%MOD
        
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

# given f(x) = (M-(x-1))^a*(x-1)^b*M^(N-a-b), f(0) = 0
# compute accumulated f(M) by Lagrange interpolation
def g(N, M, a, b, lookup):  # compute and cache, at most O(N^3) time and O(N^2) space in each test case
    if (a, b) not in lookup:  # lazy initialization
        f = [mulmod(mulmod(pow(M-(k-1), a, MOD), pow(k-1, b, MOD)), pow(M, N-a-b, MOD)) if k else 0 for k in xrange(min(a+b+1, M)+1)]
        for k in xrange(1, len(f)):
            f[k] = addmod(f[k], f[k-1])  # accumulate f
        lookup[(a, b)] = lagrange_interpolation(f, M)
    return lookup[(a, b)]

def binary_search_game():
    N, M, L = map(int, raw_input().strip().split())
    A = map(lambda x : int(x)-1, raw_input().strip().split())

    left = {A[i] for i in xrange(len(A)//2)}  # left half of board set
    right = {A[i] for i in xrange(len(A)//2, len(A))}  # right half of board set
    both = left.intersection(right)
    left = {i for i in left if i not in both}
    right = {i for i in right if i not in both}
    default_state = [1, 0] if L%2 else [0, 1]
    chosen_state = default_state[::-1]
    result, values, lookup = 0, [default_state for _ in xrange(N)], {}
    for mask_both in xrange(2**len(both)):
        left_cnt, right_cnt = Counter(), Counter()
        both_C = mask_to_set(both, mask_both)
        for i in both:
            values[i] = chosen_state if i in both_C else default_state
        for mask_left in xrange(2**len(left)):  # mask_left and mask_right are independent of states, loops O(2^(len(both)+len(left))) <= O(2^(2^L/2)) times
            left_C = mask_to_set(left, mask_left)
            for i in left:
                values[i] = chosen_state if i in left_C else default_state
            left_cnt[len(left_C)] += check(A, values, 0, (len(A)-1)//2)[0]  # alice lose, Time: O(2^L)
        for mask_right in xrange(2**len(right)):  # mask_left and mask_right are independent of states, loops O(2^(len(both)+len(right))) <= O(2^(2^L/2)) times
            right_C = mask_to_set(right, mask_right)
            for i in right:
                values[i] = chosen_state if i in right_C else default_state
            right_cnt[len(right_C)] += check(A, values, (len(A)-1)//2+1, len(A)-1)[0]  # alice lose, Time: O(2^L)
        result = addmod(result, g(N, M, len(both_C), len(both)-len(both_C), lookup))  # add all count of both_C
        for i in xrange(len(left)+1):  # O(N^2) times
            for j in xrange(len(right)+1):
                cnt = g(N, M, len(both_C)+i+j, (len(both)-len(both_C))+(len(left)-i)+(len(right)-j), lookup)
                result = submod(result, mulmod(mulmod(left_cnt[i], right_cnt[j]), cnt))  # sub lose count of both_C
    return result

MOD = 10**9+7
inv = [0, 1]
inv_fact = [1, 1]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, binary_search_game())
