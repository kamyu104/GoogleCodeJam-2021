# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 2 - Problem B. Matrygons
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dbf06
#
# Time:  precompute: O(NlogN)
#        runtime:    O(1)
# Space: O(N)
#

def matrygons():
    N = input()
    return dp[N]

MAX_N = 10**6
pseudo = [0]*(MAX_N+1)
dp = [0]*(MAX_N+1)
for i in xrange(1, MAX_N+1):
    for j in xrange(2*i, MAX_N+1, i):
        pseudo[j] = max(pseudo[j], pseudo[i-1]+1)
for i in xrange(1, MAX_N+1):
    for j in xrange(3*i, MAX_N+1, i):
        dp[j] = max(dp[j], pseudo[i-1]+1)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, matrygons())
