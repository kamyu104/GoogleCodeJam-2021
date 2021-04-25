# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1B - Problem A. Broken Clock
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae694
#
# Time:  O(logT), T is the max ticks
# Space: O(logT)
#

from itertools import permutations 

def linear_congruence(a, b, m):  # Time: O(logN), the same as gcd, Space: O(logN)
    # gcd(a, m) = 1, find x, s.t. ax % m = b % m
    # => (a%m)x = my+b
    # => gcd(m, a%m) = 1, find x, s.t. my % (a%m) = -b % (a%m)
    # => y = linear_congruence(m, -b, a%m)
    # => x = (my+b)/(a%m)
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

def format_ticks(t):
    s, n = divmod(t, TICKS_PER_SECOND)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return "%s %s %s %s" % (h, m, s, n)

def solution():
    A, B, C = map(int, raw_input().strip().split())
    # t = (h+x+1)%TOTAL
    # 12*t%TOTAL = (m+x+1)%TOTAL
    # 720*t%TOTAL = (s+x+1)%TOTAL
    # => 11*t % TOTAL = (m-h) % TOTAL
    for h, m, s in set(permutations([A, B, C])):
        t = INV_11*(m-h)%TOTAL
        if 708*t%TOTAL == (s-m)%TOTAL and 719*t%TOTAL == (s-h)%TOTAL:
            break
    return format_ticks(t)

TICKS_PER_SECOND = 10**9
TOTAL = 12*60*60*TICKS_PER_SECOND
INV_11 = linear_congruence(11, 1, TOTAL)%TOTAL
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, solution())
