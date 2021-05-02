# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem C. Double or NOTing
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c1139
#
# Time:  O(K * (|S| + |E|)), K is the number of bit groups of S
# Space: O(|E| + |S|)
#
# shorter but slower than double_or_noting.py
#

# from re import match

def flip(s):
    return "".join(["01"[c == '0'] for c in s]).lstrip('0') or "0"

def not_count(s):
    s += '0'  # if s ends with '1', it requires one more "not" operation, which could be easily counted by appending a '0'
    return sum(int(s[i] != s[i+1]) for i in reversed(xrange(len(s)-1)))

def double_or_noting():
    S, E = raw_input().strip().split()

    result = float("inf")
    X = 0
    while S != "0":
        if S == E[:len(S)] and X >= not_count(E[len(S):]):
            result = min(result, X+(len(E)-len(S)))
        S = flip(S)
        X += 1
    if X >= not_count(E):
        result = min(result, X+len(E))
    if E[0] == '0':
        result = min(result, X)
    else:
        cnt = not_count(E[1:])
        if cnt == 0:
            # assert(match("^10*$", E))
            result = min(result, X+1+(len(E)-1))  # S =X=> "0" =1=> "1" =(len(E)-1)=> "10*"
        elif cnt == 1:
            # assert(match("^11+0*$", E))
            result = min(result, X+1+len(E)+1)  # S =X=> "0" =1=> "1" =k=> "100+" =1=> "11+" =(len(E)-k)=> "11+0*", where 2 <= k <= len(E)
    return result if result != float("inf") else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, double_or_noting())
