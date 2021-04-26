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
# accuracy = 19086952424670896.00/19131995794056374.42 = 99.76%
#

from sys import stdout
from collections import defaultdict

def read():
    return input()

def write(i):
    print i
    stdout.flush()

def digit_blocks():
    zero = one = two = other = 0
    lookup = defaultdict(list)
    lookup[0] = range(N)
    for _ in xrange(N*B):
        d = read()
        h = bt[zero][one][two][other][d]
        if h == B-1:
            one -= 1
            zero +=1
        elif h == B-2:
            two -= 1
            one += 1
        else:
            other += 1
            if other == B-2:
                other = 0
                two += 1
        i = lookup[h].pop()
        lookup[h+1].append(i)
        write(i+1)
        
D = 10
T, N, B, P = map(int, raw_input().strip().split())
P = [1]
while len(P) < B:
    P.append(P[-1]*10)
dp = [[[[0.0 for _ in xrange(B-2)] for _ in xrange(N+1)] for _ in xrange(N+1)] for _ in xrange(N+1)]
bt = [[[[[None for _ in xrange(D)] for _ in xrange(B-2)] for _ in xrange(N+1)] for _ in xrange(N+1)] for _ in xrange(N+1)]
for zero in reversed(xrange(N+1)):
    for one in reversed(xrange(N-zero+1)):
        for two in reversed(xrange(N-zero-one+1)):
            for other in reversed(xrange(B-2)):
                if (zero, one, two) == (N, 0, 0) or (zero+one+two == N and other):
                    continue
                for d in xrange(D):
                    max_ex = float("-inf")
                    if one:
                        ex = dp[zero+1][one-1][two][other] + P[B-1]*d
                        if ex > max_ex:
                            max_ex = ex
                            bt[zero][one][two][other][d] = B-1
                    if two:
                        ex = dp[zero][one+1][two-1][other] + P[B-2]*d
                        if ex > max_ex:
                            max_ex = ex
                            bt[zero][one][two][other][d] = B-2
                    if zero+one+two != N:
                        if other == B-3:
                            ex = dp[zero][one][two+1][0] + P[other]*d
                            if ex > max_ex:
                                max_ex = ex
                                bt[zero][one][two][other][d] = other
                        else:
                            ex = dp[zero][one][two][other+1] + P[other]*d
                            if ex > max_ex:
                                max_ex = ex
                                bt[zero][one][two][other][d] = other
                    dp[zero][one][two][other] += max_ex/10
MAX_SCORE = 19131995794056374.42
assert(dp[0][0][0][0]/MAX_SCORE >= 0.9976)
for case in xrange(T):
    digit_blocks()
