# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1B - Problem A. Broken Clock
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae694
#
# Time:  O(1)
# Space: O(1)
#

from itertools import permutations

def linear_congruence(a, m, b):  # Time: O(logN), the same as gcd, Space: O(logN)
    # gcd(a, m) = g and g|b, find x, s.t. ax % m = b % m
    # => (a%m)x = my+(b%m)
    # => gcd(m, a%m) = g and g|-(b%m), find y, s.t. my % (a%m) = -(b%m) % (a%m)
    # => y = linear_congruence(m, a%m, -(b%m))
    # => x = (my+(b%m))/(a%m)
    ambs = []
    while m:
        a, m, b = m, a%m, -(b%m)
        if m:
            ambs.append((m, a, -b))
    x = a  # a is gcd
    while ambs:
        a, m, b = ambs.pop()
        x = (m*x+b)//a
    return x

def format_ticks(t):
    s, n = divmod(t, TICKS_PER_SECOND)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return "%s %s %s %s" % (h, m, s, n)

def solution():
    A, B, C = map(int, raw_input().strip().split())
    # t%TOTAL = (h+x)%TOTAL
    # 12*t%TOTAL = (m+x)%TOTAL
    # 720*t%TOTAL = (s+x)%TOTAL
    # => find t s.t.
    # 11*t%TOTAL = (m-h)%TOTAL
    # 708*t%TOTAL = (s-m)%TOTAL
    for h, m, s in set(permutations([A, B, C])):
        t = INV_11*(m-h)%TOTAL
        if 708*t%TOTAL == (s-m)%TOTAL:
            break
    return format_ticks(t)

TICKS_PER_SECOND = 10**9
TOTAL = 12*60*60*TICKS_PER_SECOND
INV_11 = linear_congruence(11, TOTAL, 1)%TOTAL  # Time: O(log(min(11, TOTAL))) = O(log11) = O(1)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, solution())
