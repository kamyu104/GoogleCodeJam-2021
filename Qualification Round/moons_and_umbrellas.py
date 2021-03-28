# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem B. Moons and Embrellas 
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145
#
# Time:  O(N)
# Space: O(1)
#

def moons_and_umbrellas():
    X, Y, S = raw_input().strip().split()
    X, Y = int(X), int(Y)
    dp = {}
    prev = None
    for c in S:
        new_dp = {}
        for i, j, cost in [('C', 'J', Y), ('J', 'C', X)]:
            if c == j:
                new_dp[i] = INF
            elif prev is None:
                new_dp[i] = 0
            elif prev == i:
                new_dp[i] = dp[i]
            elif prev == j:
                new_dp[i] = dp[j]+cost
            elif prev == '?':
                new_dp[i] = min(dp[i], dp[j]+cost)
        dp = new_dp
        prev = c
    return min(dp.itervalues())

INF = float("inf")
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, moons_and_umbrellas())
