# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem A. Closest Pick
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f00
#
# Time:  O(NlogN)
# Space: O(N)
#

def closest_pick():
    N, K = map(int, raw_input().strip().split())
    P = sorted(set(map(int, raw_input().strip().split())))

    result = prev_max = P[0]-1  # one or two in the first interval
    for i in xrange(1, len(P)):
        result = max(result, prev_max+(P[i]-P[i-1])//2, P[i]-P[i-1]-1)  # one or two in this interval
        prev_max = max(prev_max, (P[i]-P[i-1])//2)
    return float(max(result, prev_max+(K-P[-1])))/K  # one or two in the last interval

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, closest_pick())
