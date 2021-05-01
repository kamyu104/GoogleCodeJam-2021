# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem A. Broken Clock
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00
#
# Time:  O(NlogN)
# Space: O(N)
#

def closest_pick():
    N, K = map(int, raw_input().strip().split())
    P = set(map(int, raw_input().strip().split()))
    if len(P) == K:
        return 0.0

    P = sorted(P)
    result = prev_max = P[0]-1
    for i in xrange(1, len(P)):
        result = max(result, prev_max+(P[i]-P[i-1])//2, P[i]-P[i-1]-1)  # two in different intervals or two in the same interval
        prev_max = max(prev_max, (P[i]-P[i-1])//2)
    result = max(result, prev_max+(K-P[-1]))
    return float(result)/K

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, closest_pick())
