# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1B - Problem C. Digit Blocks
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae37b
#
# Time:  precompute: O(N^3 * B * D)
#        runtime:    O(N * B)
# Space: O(N^3 * B * D)
#
# Usage: python interactive_runner.py python3 testing_tool.py 1 -- python digit_blocks.py
#
# Expected score compared to the max expected score = 19086952424670896.00/19131995794056374.42 = 99.76%
#

from sys import stdout

def read():
    return input()

def write(i):
    print i
    stdout.flush()

def digit_blocks():
    grow_h = 0
    lookup =  [[] for _ in xrange(B+1)]
    lookup[0] = range(N)
    for _ in xrange(N*B):
        d = read()
        h = choice[len(lookup[B])][len(lookup[B-1])][len(lookup[B-2])][grow_h][d]
        if h < B-2:
            grow_h = (grow_h+1)%(B-2)
        lookup[h+1].append(lookup[h].pop())
        write(lookup[h+1][-1]+1)
        
D = 10
T, N, B, P = map(int, raw_input().strip().split())
P = [1]
while len(P) < B:
    P.append(P[-1]*D)
dp = [[[[0.0 for _ in xrange(B-2)] for _ in xrange(N+1)] for _ in xrange(N+1)] for _ in xrange(N+1)]
choice = [[[[[None for _ in xrange(D)] for _ in xrange(B-2)] for _ in xrange(N+1)] for _ in xrange(N+1)] for _ in xrange(N+1)]
for remain0_cnt in reversed(xrange(N)):
    for remain1_cnt in reversed(xrange(N-remain0_cnt+1)):
        for remain2_cnt in reversed(xrange(N-remain0_cnt-remain1_cnt+1)):
            for grow_h in reversed(xrange(1 if remain0_cnt+remain1_cnt+remain2_cnt == N else B-2)):
                for d in xrange(D):
                    max_ev = float("-inf")
                    if remain1_cnt:
                        ev = dp[remain0_cnt+1][remain1_cnt-1][remain2_cnt][grow_h] + P[B-1]*d
                        if ev > max_ev:
                            max_ev = ev
                            choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d] = B-1
                    if remain2_cnt:
                        ev = dp[remain0_cnt][remain1_cnt+1][remain2_cnt-1][grow_h] + P[B-2]*d
                        if ev > max_ev:
                            max_ev = ev
                            choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d] = B-2
                    if remain0_cnt+remain1_cnt+remain2_cnt != N:
                        ev = dp[remain0_cnt][remain1_cnt][remain2_cnt+(grow_h+1)//(B-2)][(grow_h+1)%(B-2)] + P[grow_h]*d
                        if ev > max_ev:
                            max_ev = ev
                            choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d] = grow_h
                    dp[remain0_cnt][remain1_cnt][remain2_cnt][grow_h] += max_ev/D
S = 19131995794056374.42
assert(dp[0][0][0][0]/S >= 0.9976)
for case in xrange(T):
    digit_blocks()
