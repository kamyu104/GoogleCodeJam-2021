# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem A. Reversort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c
#
# Time:  O(N^2)
# Space: O(1)
#

def min_idx(L, i):
    m = i
    for j in xrange(i, len(L)):
        if L[j] < L[m]:
            m = j
    return m

def reverse(L, i, j):
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1
    
def reversort():
    N = input()
    L = map(int, raw_input().strip().split())

    result = 0
    for i in xrange(len(L)-1):
        # m = L.index(min(L[i:])) # Space: O(N)
        m = min_idx(L, i)  # Space: O(1)
        # L[i:m+1] = L[i:m+1][::-1]  # Space: O(N) 
        reverse(L, i, m)  # Space: O(1)
        result += m-i+1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reversort())
