# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1A - Problem A. Append Sort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5
#
# Time:  O(N * log(MAX_X))
# Space: O(log(MAX_X))
#

def append_sort():
    N = input()
    X = map(list, raw_input().strip().split())

    result = 0
    curr = list(X[0])
    for i in xrange(1, len(X)):
        prev, curr = curr, list(X[i])
        if len(curr) > len(prev):
            continue
        result += (len(prev)-len(curr))
        if curr[:len(curr)] < prev[:len(curr)]:
            curr.extend(['0']*((len(prev)-len(curr))+1))
            result += 1
        elif curr[:len(curr)] > prev[:len(curr)]:
            curr.extend(['0']*(len(prev)-len(curr)))
        else:
            if len(prev)-len(curr) != 0 and int("".join(prev[len(curr):]))+1 < 10**(len(prev)-len(curr)):
                curr.extend(list(str(int("".join(prev[len(curr):]))+1).zfill((len(prev)-len(curr)))))
            else:
                curr.extend(['0']*((len(prev)-len(curr))+1))
                result += 1
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, append_sort())
