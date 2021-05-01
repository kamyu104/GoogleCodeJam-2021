# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem C. Double or NOTthing
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c1139
#
# Time:  O(K * S)
# Space: O(S)
#

from itertools import groupby

def flip(s):
    return "".join([('1' if c == '0' else '0') for c in s]).lstrip('0') or '0'

def change_count(s):
    return sum(int(s[i] != s[i+1]) for i in xrange(len(s)-1))

def check(X, suffix):
    return X >= change_count(suffix)

def double_or_nothing():
    S, E = raw_input().strip().split()

    result = float("inf")
    prefix = S
    X = 0
    while prefix != "0":
        if prefix != E[:len(prefix)]:
            prefix = flip(prefix)
            X += 1
            continue
        suffix = E[len(prefix):]
        if not check(X, suffix+'0'):
            prefix = flip(prefix)
            X += 1
            continue
        result = min(result, X+len(suffix))
        prefix = flip(prefix)
        X += 1
    if check(X, E+'0'):
        result = min(result, X+len(E))
    if E == '0':
        result = min(result, X)
    elif E[0] == '1':
        if len(E) == 1:
            result = min(result, X+1)
        else:
            if E[1:] == '0'*(len(E)-1):  # 10..0
                result = min(result, X+1+(len(E)-1))
            elif change_count(E) <= 1:  # 110..0, ..., 111..10, 111..1
                result = min(result, X+1+len(E)+1)
    return "IMPOSSIBLE" if result == float("inf") else result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, double_or_nothing())
