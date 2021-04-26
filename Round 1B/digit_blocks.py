# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1B - Problem C. Digit Blocks
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae37b
#
# Time:  precompute: O(N^3 * B * D)
#        runtime:    O(N * B)
# Space: O(N^3 * B * D)
# Usage: python interactive_runner.py python3 testing_tool.py 1 -- python digit_blocks.py
#
# P = 19086952424670896.00/19131995794056374.42 = 99.76%
#

from sys import stdout
from collections import defaultdict

def read():
    return input()

def write(i):
    print i
    stdout.flush()

def digit_blocks():
    remain0_cnt = remain1_cnt = remain2_cnt = grow_h = 0
    lookup = defaultdict(list)
    lookup[0] = range(N)
    for _ in xrange(N*B):
        d = read()
        h = choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d]
        if h == B-1:
            remain1_cnt -= 1
            remain0_cnt +=1
        elif h == B-2:
            remain2_cnt -= 1
            remain1_cnt += 1
        else:
            grow_h += 1
            if grow_h == B-2:
                grow_h = 0
                remain2_cnt += 1
        lookup[h+1].append(lookup[h].pop())
        write(lookup[h+1][-1]+1)
        
D = 10
T, N, B, P = map(int, raw_input().strip().split())
P = [1]
while len(P) < B:
    P.append(P[-1]*10)
dp = [[[[0.0 for _ in xrange(B-2)] for _ in xrange(N+1)] for _ in xrange(N+1)] for _ in xrange(N+1)]
choice = [[[[[None for _ in xrange(D)] for _ in xrange(B-2)] for _ in xrange(N+1)] for _ in xrange(N+1)] for _ in xrange(N+1)]
for remain0_cnt in reversed(xrange(N+1)):
    for remain1_cnt in reversed(xrange(N-remain0_cnt+1)):
        for remain2_cnt in reversed(xrange(N-remain0_cnt-remain1_cnt+1)):
            for grow_h in reversed(xrange(B-2)):
                if (remain0_cnt, remain1_cnt, remain2_cnt) == (N, 0, 0) or (remain0_cnt+remain1_cnt+remain2_cnt == N and grow_h):
                    continue
                for d in xrange(D):
                    max_ex = float("-inf")
                    if remain1_cnt:
                        ex = dp[remain0_cnt+1][remain1_cnt-1][remain2_cnt][grow_h] + P[B-1]*d
                        if ex > max_ex:
                            max_ex = ex
                            choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d] = B-1
                    if remain2_cnt:
                        ex = dp[remain0_cnt][remain1_cnt+1][remain2_cnt-1][grow_h] + P[B-2]*d
                        if ex > max_ex:
                            max_ex = ex
                            choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d] = B-2
                    if remain0_cnt+remain1_cnt+remain2_cnt != N:
                        if grow_h == B-3:
                            ex = dp[remain0_cnt][remain1_cnt][remain2_cnt+1][0] + P[grow_h]*d
                            if ex > max_ex:
                                max_ex = ex
                                choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d] = grow_h
                        else:
                            ex = dp[remain0_cnt][remain1_cnt][remain2_cnt][grow_h+1] + P[grow_h]*d
                            if ex > max_ex:
                                max_ex = ex
                                choice[remain0_cnt][remain1_cnt][remain2_cnt][grow_h][d] = grow_h
                    dp[remain0_cnt][remain1_cnt][remain2_cnt][grow_h] += max_ex/10
S = 19131995794056374.42
assert(dp[0][0][0][0]/S >= 0.9976)
for case in xrange(T):
    digit_blocks()
