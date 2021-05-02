# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem C. Double or NOTing
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c1139
#
# Time:  O(|E| + K * |S|), K is the number of bit groups of S
# Space: O(|S|)
#

# from re import match

def flip(s):
    return "".join(["01"[c == '0'] for c in s]).lstrip('0') or "0"

def init_flip_count(E):
    s = E+'0'  # if s ends with '1', it requires one more "not" operation (flip), which could be easily counted by appending a '0'
    suffix_cnt = [0]*len(s)
    for i in reversed(xrange(len(s)-1)):
        suffix_cnt[i] = suffix_cnt[i+1] + int(s[i] != s[i+1])
    return suffix_cnt

def get_flip_count(suffix_cnt, i):
    return suffix_cnt[i] if i < len(suffix_cnt) else 0

def double_or_noting():
    S, E = raw_input().strip().split()

    suffix_cnt = init_flip_count(E)
    result = float("inf")
    X = 0
    while S != "0":
        if S == E[:len(S)] and X >= get_flip_count(suffix_cnt, len(S)):
            result = min(result, X+len(E[len(S):]))
        S = flip(S)
        X += 1
    if X >= get_flip_count(suffix_cnt, 0):
        result = min(result, X+len(E))
    if E[0] == '0':
        result = min(result, X)
    else:
        cnt = get_flip_count(suffix_cnt, 1)
        if cnt == 0:
            # assert(match("^10*$", E))
            result = min(result, X+1+(len(E)-1))  # S =X=> "0" =1=> "1" =(len(E)-1)=> "10*"
        elif cnt == 1:
            # assert(match("^11+0*$", E))
            result = min(result, X+1+len(E)+1)  # S =X=> "0" =1=> "1" =k=> "100+" =1=> "11+" =(len(E)-k)=> "11+0*", where 2 <= k <= len(E)
    return result if result != float("inf") else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, double_or_noting())
