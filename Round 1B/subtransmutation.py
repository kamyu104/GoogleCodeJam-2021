# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1B - Problem B. Subtransmutation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae4aa
#
# Time:  O(MAX_M^2), MAX_M is the max possible m in the given limit
# Space: O(MAX_M)
#

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
    result = N+1
    while result <= MAX_M:
        if check(A, B, U, result):
            return result
        result += 1
    return "IMPOSSIBLE"

'''
GUESS = 1000
MAX_N = MAX_U = 20
MAX_A = MAX_B = 20
U = [MAX_U]*MAX_N
MAX_M = 0
for A in xrange(1, MAX_A+1):
    for B in xrange(A+1, MAX_B+1):
        result = MAX_N+1
        while result <= GUESS:
            if check(A, B, U, result):
                MAX_M = max(MAX_M, result)
                break
            result += 1
assert(MAX_M == 402)
'''
MAX_M = 402
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, subtransmutation())
