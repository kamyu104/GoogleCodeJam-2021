# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals - Problem D. Divisible Divisions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084fb3a
#
# Time:  O(|S|logD + D)
# Space: O(|S| + D)
#

from collections import Counter

def addmod(a, b):
    return (a+b)%MOD

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

    suffix = [0]*(len(S)+1)
    basis = 1
    for i in reversed(xrange(len(S))):
        suffix[i] = (suffix[i+1] + S[i]*basis) % d_remain
        basis = basis*10 % d_remain

    # dp1[i]: count of divisible divisions of this prefix whose last division is divisible by D ends at S[i-1]
    # dp2[i]: count of divisible divisions of this prefix whose last division is not divisible by D ends at S[i-1]
    dp1, dp2 = [[0]*(len(S)+1) for _ in xrange(2)]
    dp1[0] = 1
    prefix_total, prefix_dp1 = [[0]*d_remain for _ in xrange(2)]
    accu_dp1, d_2_5 = 1, D//d_remain
    for i in xrange(1, len(S)+1):
        dp2[i] = accu_dp1
        curr, basis = 0, 1
        for k in xrange(1, l+1):  # O(logD) times
            if i-k < 0:
                break
            j = i-k
            curr = (curr + S[j]*basis) % d_2_5
            if k == l:
                prefix_total[suffix[j]] = addmod(prefix_total[suffix[j]], addmod(dp1[j], dp2[j]))
                prefix_dp1[suffix[j]] = addmod(prefix_dp1[suffix[j]], dp1[j])
                if curr == 0:
                    # since all(S[j:i]%d_2_5 == 0 for j in xrange(i-l+1)) is true,
                    # find sum(cnt[j] for j in xrange(i-l+1) if suffix[j] == suffix[i]) <=> find sum(cnt[j] for j in xrange(i-l+1) if S[j:i]%D == 0)
                    dp1[i] = addmod(dp1[i], prefix_total[suffix[i]])  # prefix_total[suffix[i]] = sum(dp1[j]+dp2[j] for j in xrange(i-l+1) if suffix[j] == suffix[i])%MOD
                    dp2[i] = addmod(dp2[i], -prefix_dp1[suffix[i]])   # prefix_dp1[suffix[i]]   = sum(dp1[j]        for j in xrange(i-l+1) if suffix[j] == suffix[i])%MOD
                break
            if curr == 0 and suffix[j] == suffix[i]:  # (S[j:i]%d_2_5 == 0) and (suffix[j]-suffix[i] == 0 <=> S[j:i]%d_remain == 0) <=> S[j:i]%D == 0
                dp1[i] = addmod(dp1[i], addmod(dp1[j], dp2[j]))
                dp2[i] = addmod(dp2[i], -dp1[j])
            basis = basis*10 % d_2_5
        accu_dp1 = addmod(accu_dp1, dp1[i])
    return addmod(dp1[len(S)], dp2[len(S)])

MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, divisible_divisions())
