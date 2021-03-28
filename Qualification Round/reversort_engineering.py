# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem C. Reversort Engineering
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
#
# Time:  O(N^2)
# Space: O(1)
#

def reverse(L, i, j):
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1

def reversort_engineering():
    N, C = map(int, raw_input().strip().split())

    if not (N-1 <= C <= (N+2)*(N-1)//2):
        return "IMPOSSIBLE"
    result = range(1, N+1)
    for i in reversed(xrange(N-1)):
        l = min(C-i, N-i)  # greedy
        C -= l
        # result[i:i+l] = result[i:i+l][::-1]  # Space: O(N)
        reverse(result, i, i+l-1)  # Space: O(1)
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reversort_engineering())
