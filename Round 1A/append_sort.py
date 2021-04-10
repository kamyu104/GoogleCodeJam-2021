# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1A - Problem A. Append Sort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5
#
# Time:  O(N * log(MAX_X) * size(int)) = O(N * log(MAX_X))
# Space: O(size(int)) = O(1)
#

def append_sort():
    N = input()
    X = map(int, raw_input().strip().split())

    result = 0
    for i in xrange(1, len(X)):
        cnt = 0
        while X[i] <= X[i-1]:
            X[i] *= 10
            cnt += 1
        if cnt > 1 and (X[i]//10) + (10**(cnt-1)-1) > X[i-1]:
            X[i] = X[i-1]+1
            cnt -= 1
        result += cnt
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, append_sort())
