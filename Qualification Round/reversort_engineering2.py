# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem C. Reversort Engineering
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
#
# Time:  O(N)
# Space: O(1)
#

def reversort_engineering():
    N, C = map(int, raw_input().strip().split())

    if not (N-1 <= C <= (N+2)*(N-1)//2):
        return "IMPOSSIBLE"
    result = [0]*N
    for i in xrange(N):
        l = min(C-(N-1-i)+1, N-i)  # greedy
        C -= l
        fill = (list(reversed(range(i+1, i+1+l))) + range(i+1+l, N+1)) if l != N-i else [i+1]
        if i%2 == 0:
            result[N-1-i//2+1-len(fill):N-1-i//2+1] = fill
        else:
            result[i//2:i//2+len(fill)] = fill[::-1]
        if l != N-i:
            break
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reversort_engineering())
