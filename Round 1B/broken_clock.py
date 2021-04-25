# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1B - Problem A. Broken Clock
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae694
#
# Time:  O(logC)
# Space: O(logC)
#

from itertools import permutations 

def linear_congruence(a, b, m):  # Time: O(logN), the same as gcd, Space: O(logN)
    # gcd(a, m) = 1, find x, s.t. ax % m = b % m
    # => ax = my+b
    # => my % a = -b % m
    # => y = linear_congruence(m, -b, a)
    # => x = (my+b)/a
    abms = []
    while m:
        a, m, b = m, a%m, -(b%m)
        if m:
            abms.append((m, -b, a))
    x = a
    while abms:
        a, b, m = abms.pop()
        x = (m*x+b)//a
    return x

def solution():
    A, B, C = map(int, raw_input().strip().split())
    # t = (h+x+1)%TOTAL
    # 12*t%TOTAL = (m+x+1)%TOTAL
    # 720*t%TOTAL = (s+x+1)%TOTAL
    # => 59*X%TOTAL = ((S-60*M)-59)%TOTAL
    for h, m, s in set(permutations([A, B, C])):
        x = linear_congruence(59, (s-60*m)-59, TOTAL)
        t = (h+x+1)%TOTAL
        if (12*t%TOTAL == (m+x+1)%TOTAL) and (720*t%TOTAL == (s+x+1)%TOTAL):
            break
    t, n = divmod(t, TICK_PER_SECOND)
    return "%s %s %s %s" % (t//3600, (t//60)%60, t%60, n)

TICK_PER_SECOND = 10**9
TOTAL = 12*60*60*TICK_PER_SECOND
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, solution())
