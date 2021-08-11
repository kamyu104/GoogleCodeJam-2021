# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals- Problem D. Divisible Divisions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084fb3a
#
# Time:  O(|S|logD)
# Space: O(D)
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

    w = l+1
    dp1, dp2 = [[0]*w for _ in xrange(2)]
    dp1[0] = 1
    prefix_total, prefix_dp1 = [[0]*d_remain for _ in xrange(2)]
    accu_dp1, d_2_5 = 1, D//d_remain
    for i in xrange(1, len(S)+1):
        dp1[i%w], dp2[i%w] = 0, accu_dp1
        curr, basis = 0, 1
        for k in xrange(1, l+1):  # O(logD) times
            if i-k < 0:
                break
            j = i-k
            curr = (curr + S[j]*basis) % d_2_5
            if k == l:
                prefix_total[suffix[j]] = addmod(prefix_total[suffix[j]], addmod(dp1[j%w], dp2[j%w]))
                prefix_dp1[suffix[j]] = addmod(prefix_dp1[suffix[j]], dp1[j%w])
                if curr % d_2_5 == 0:
                    dp1[i%w] = addmod(dp1[i%w], prefix_total[suffix[i]])
                    dp2[i%w] = addmod(dp2[i%w], -prefix_dp1[suffix[i]])
                break
            if curr == 0 and suffix[j] == suffix[i]:
                dp1[i%w] = addmod(dp1[i%w], addmod(dp1[j%w], dp2[j%w]))
                dp2[i%w] = addmod(dp2[i%w], -dp1[j%w])
            basis = basis*10 % d_2_5
        accu_dp1 = addmod(accu_dp1, dp1[i%w])
    return addmod(dp1[len(S)%w], dp2[len(S)%w])

MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, divisible_divisions())
