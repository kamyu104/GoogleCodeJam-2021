# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals- Problem D. Divisible Divisions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084fb3a
#
# Time:  O(|S|logD)
# Space: O(D)
#

def addmod(a, b):
    return (a+b)%MOD

def submod(a, b):
    return (a-b)%MOD

def mulmod(a, b):
    return (a*b)%MOD

def divisible_divisions():
    S, D = raw_input().strip().split()
    s = S
    S, D = map(int, list(S)), int(D)
    d_remain, d_2_5, cnt_2 = D, 1, 0
    while d_remain%2 == 0:
        d_remain //= 2
        cnt_2 += 1
        d_2_5 *= 2
    cnt_5 = 0
    while d_remain%5 == 0:
        d_remain //= 5
        cnt_5 += 1
        d_2_5 *= 5
    l = max(1, cnt_2, cnt_5)
    suffix = [0]*(len(S)+1)
    basis = 1
    for i in reversed(xrange(len(S))):
        suffix[i] = (suffix[i+1] + S[i]*basis) % d_remain
        basis = basis*10 % d_remain
    dp1, dp2 = [[0]*(l+1) for _ in xrange(2)]
    dp1[0] = 1
    prefix_total, prefix_dp1 = [[0]*d_remain for _ in xrange(2)]
    accu_dp1 = 1
    for i in xrange(1, len(S)+1):
        dp1[i%(l+1)], dp2[i%(l+1)] = 0, accu_dp1
        curr, basis = 0, 1
        for k in xrange(1, l+1):  # Time:  O(logD)
            if i-k < 0:
                break
            j = i-k
            curr = (curr + S[j]*basis) % d_2_5
            if k == l:
                prefix_total[suffix[j]] = addmod(prefix_total[suffix[j]], addmod(dp1[j%(l+1)], dp2[j%(l+1)]))
                prefix_dp1[suffix[j]] = addmod(prefix_dp1[suffix[j]], dp1[j%(l+1)])
                if curr % d_2_5 == 0:
                    dp1[i%(l+1)] = addmod(dp1[i%(l+1)], prefix_total[suffix[i]])
                    dp2[i%(l+1)] = submod(dp2[i%(l+1)], prefix_dp1[suffix[i]])
                break
            if curr == 0 and suffix[j] == suffix[i]:
                dp1[i%(l+1)] = addmod(dp1[i%(l+1)], addmod(dp1[j%(l+1)], dp2[j%(l+1)]))
                dp2[i%(l+1)] = submod(dp2[i%(l+1)], dp1[j%(l+1)])
            basis = basis*10 % d_2_5
        accu_dp1 = addmod(accu_dp1, dp1[i%(l+1)])
    return addmod(dp1[len(S)%(l+1)], dp2[len(S)%(l+1)])

MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, divisible_divisions())
