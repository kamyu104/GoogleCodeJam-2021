# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem C. Reversort Engineering
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7
#
# Time:  O(N^2)
# Space: O(N)
#

def reversort_engineering():
    N, C = map(int, raw_input().strip().split())

    if not (N-1 <= C <= (N+2)*(N-1)//2):
        return "IMPOSSIBLE"
    operations = []
    for i in xrange(N-1):
        operations.append(min(C-(N-1-i)+1, N-i))  # greedy
        C -= operations[-1]
    result = range(1, N+1)
    for i in reversed(xrange(N-1)):
        result[i:i+operations[i]] = result[i:i+operations[i]][::-1]
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reversort_engineering())
