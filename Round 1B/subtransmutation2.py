# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1B - Problem A. Broken Clock
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae694
#
# Time:  O(MAX_M^2), MAX_M is the max possible m in the given limit
# Space: O(MAX_M)
#

from fractions import gcd

def get_U(U, i):
    return U[i] if i < len(U) else 0

def check(A, B, U, x):
    count = [0]*x
    count[-1] = 1
    for i in reversed(xrange(len(count))):
        if count[i] < get_U(U, i):
            return False
        extra = count[i]-get_U(U, i)
        if A <= i:
            count[i-A] += extra
        if B <= i:
            count[i-B] += extra
    return True

def subtransmutation():
    N, A, B = map(int, raw_input().strip().split())
    U = map(int, raw_input().strip().split())
    g = gcd(A, B)
    k = None
    for i, c in enumerate(U, 1):
        if not c:
            continue
        if k is None:
            k = i%g
            continue
        if i%g != k:
            return "IMPOSSIBLE" 
    result = (N+1)+(k-(N+1))%g
    while not check(A, B, U, result):
        result += g
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, subtransmutation())
