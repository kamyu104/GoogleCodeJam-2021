# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem C. Reversort Engineering
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
#
# Time:  O(N)
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
    result = [0]*N
    for i in xrange(N):
        l = min(C-(N-1-i)+1, N-i)  # greedy
        C -= l
        if l != N-i:
            break
        if i%2 == 0:
            result[N-1-i//2] = i+1
        else:
            result[i//2] = i+1
    if i%2 == 0:
        k = i+1
        for j in xrange((N-1-i//2+1)-(N-i), N-1-i//2+1):
            result[j] = k
            k += 1
        reverse(result, (N-1-i//2+1)-(N-i), ((N-1-i//2+1)-(N-i))+l-1)
    else:
        k = i+1
        for j in reversed(xrange(i//2, i//2+(N-i))):
            result[j] = k
            k += 1
        reverse(result, (i//2+(N-i)-1)-l+1, i//2+(N-i)-1)
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reversort_engineering())
