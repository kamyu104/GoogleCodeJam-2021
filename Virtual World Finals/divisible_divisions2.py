# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals - Problem D. Divisible Divisions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084fb3a
#
# Time:  O(|S|logD)
# Space: O(min(|S|logD, D))
#
# Time and Space optimized from divisible_divisions.py
#

from collections import Counter

def addmod(a, b):
    return (a+b)%MOD

# Template:
# https://github.com/kamyu104/GoogleCodeJam-2021/blob/main/Round%201B/broken_clock.py
def linear_congruence(a, m, b):  # Time: O(logN), the same as gcd, Space: O(logN)
    # gcd(a, m) = g and g|b, find x, s.t. ax % m = b % m
    # => (a%m)x = my+(b%m)
    # => gcd(m, a%m) = g and g|-(b%m), find y, s.t. my % (a%m) = -(b%m) % (a%m)
    # => y = linear_congruence(m, a%m, -(b%m))
    # => x = (my+(b%m))/(a%m)
    ambs = []
    while m:
        a, m, b = m, a%m, -(b%m)
        if m:
            ambs.append((m, a, -b))
    x = a  # a is gcd
    while ambs:
        a, m, b = ambs.pop()
        x = (m*x+b)//a
    return x

def divisible_divisions():
    S, D = raw_input().strip().split()
    S, D = map(int, list(S)), int(D)

    cnts = Counter([1])
    d_remain = D
    for p in [2, 5]:
        while d_remain%p == 0:
            d_remain //= p
            cnts[p] += 1
    l = max(cnts.itervalues())  # l = O(logD)

    curr1, basis1 = 0, 1
    for i in reversed(xrange(len(S))):
        curr1 = (curr1 + S[i]*basis1) % d_remain
        basis1 = basis1*10 % d_remain

    # dp1[i]: count of divisible divisions of this prefix whose last division is divisible by D ends at S[i-1]
    # dp2[i]: count of divisible divisions of this prefix whose last division is not divisible by D ends at S[i-1]
    w = l+1
    dp1, dp2, suffix = [[0]*w for _ in xrange(3)]
    dp1[0], suffix[0] = 1, curr1
    prefix_total, prefix_dp1 = [Counter() for _ in xrange(2)]
    accu_dp1, d_2_5 = 1, D//d_remain
    inv_10_mod_d_remain = linear_congruence(10, d_remain, 1)%d_remain  # Time: O(logD)
    for i in xrange(1, len(S)+1):
        basis1 = basis1*inv_10_mod_d_remain % d_remain
        curr1 = (curr1 - S[i-1]*basis1) % d_remain
        dp1[i%w], dp2[i%w], suffix[i%w] = 0, accu_dp1, curr1
        curr2, basis2 = 0, 1
        for k in xrange(1, l+1):  # O(logD) times
            if i-k < 0:
                break
            j = i-k
            curr2 = (curr2 + S[j]*basis2) % d_2_5
            if k == l:
                prefix_total[suffix[j%w]] = addmod(prefix_total[suffix[j%w]], addmod(dp1[j%w], dp2[j%w]))
                prefix_dp1[suffix[j%w]] = addmod(prefix_dp1[suffix[j%w]], dp1[j%w])
                if curr2 == 0:
                    # since all(S[j:i]%d_2_5 == 0 for j in xrange(i-l+1)) is true,
                    # find sum(cnt[j] for j in xrange(i-l+1) if suffix[j] == suffix[i]) <=> find sum(cnt[j] for j in xrange(i-l+1) if S[j:i]%D == 0)
                    dp1[i%w] = addmod(dp1[i%w], prefix_total[suffix[i%w]])  # prefix_total[suffix[i]] = sum(dp1[j]+dp2[j] for j in xrange(i-l+1) if suffix[j] == suffix[i])%MOD
                    dp2[i%w] = addmod(dp2[i%w], -prefix_dp1[suffix[i%w]])   # prefix_dp1[suffix[i]]   = sum(dp1[j]        for j in xrange(i-l+1) if suffix[j] == suffix[i])%MOD
                break
            if curr2 == 0 and suffix[j%w] == suffix[i%w]:  # (S[j:i]%d_2_5 == 0) and (suffix[j]-suffix[i] == 0 <=> S[j:i]*10^(i-j)%d_remain == 0 == S[j:i]%d_remain) <=> S[j:i]%D == 0
                dp1[i%w] = addmod(dp1[i%w], addmod(dp1[j%w], dp2[j%w]))
                dp2[i%w] = addmod(dp2[i%w], -dp1[j%w])
            basis2 = basis2*10 % d_2_5
        accu_dp1 = addmod(accu_dp1, dp1[i%w])
    return addmod(dp1[len(S)%w], dp2[len(S)%w])

MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, divisible_divisions())
