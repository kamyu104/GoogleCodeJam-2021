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
    dp = [INF]*2
    prev = None
    for c in S:
        new_dp = [INF]*2
        if c != 'J':
            if prev is None:
                new_dp[C] = 0
            elif prev == 'C':
                new_dp[C] = dp[C]
            elif prev == 'J':
                new_dp[C] = dp[J]+Y  # JC
            elif prev == '?':
                new_dp[C] = min(dp[C], dp[J]+Y)  # CC or JC
        if c != 'C':
            if prev is None:
                new_dp[J] = 0
            elif prev == 'C':
                new_dp[J] = dp[C]+X  # CJ
            elif prev == 'J':
                new_dp[J] = dp[J]
            elif prev == '?':
                new_dp[J] = min(dp[J], dp[C]+X)  # JJ or CJ
        dp = new_dp
        prev = c
    return min(dp)

INF = float("inf")
C, J = range(2)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, moons_and_umbrellas())
