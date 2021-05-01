# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem C. Double or NOTthing
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c1139
#
# Time:  O(K * len(S)), K is the number of bit groups of S
# Space: O(len(S))
#

from itertools import groupby

def flip(s):
    return "".join([('1' if c == '0' else '0') for c in s]).lstrip('0') or '0'

def change_count(s):
    return sum(int(s[i] != s[i+1]) for i in xrange(len(s)-1))

def double_or_nothing():
    S, E = raw_input().strip().split()

    result = float("inf")
    X = 0
    while S != "0":
        if S == E[:len(S)] and X >= change_count(E[len(S):]+'0'):
            result = min(result, X+len(E[len(S):]))
        S = flip(S)
        X += 1
    if X >= change_count(E+'0'):
        result = min(result, X+len(E))
    if E == '0':
        result = min(result, X)
    elif E[0] == '1':
        if len(E) == 1:  # case of 1
            result = min(result, X+1)
        else:
            if E[1:] == '0'*(len(E)-1):  # case of 10..0
                result = min(result, X+1+(len(E)-1))
            elif change_count(E) <= 1:  # cases of 110..0, ..., 111..10, 111..1
                result = min(result, X+1+len(E)+1)
    return "IMPOSSIBLE" if result == float("inf") else result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, double_or_nothing())
