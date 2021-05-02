# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C-Problem C. Double or NOTing
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c1139
#
# Time:  O(|E| + |S|), K is the number of bit groups of S
# Space: O(|E| + |S|)
#
# KMP solution
#

# from re import match

def modified_KMP(text, pattern, prefix, flag):
    j = -1
    for i in xrange(len(text)):
        while j != -1 and pattern[j+1] != text[i]^flag:
            j = prefix[j]
        if pattern[j+1] == text[i]^flag:
                j += 1
        if j+1 == len(pattern):
            if i != len(text)-1:
                j = prefix[j]
    return j  # pattern[:j+1] is the longest suffix of text

def getPrefix(pattern):
    prefix = [-1]*len(pattern)
    j = -1
    for i in xrange(1, len(pattern)):
        while j != -1 and pattern[j+1] != pattern[i]:
            j = prefix[j]
        if pattern[j+1] == pattern[i]:
            j += 1
        prefix[i] = j
    return prefix

def init_flip_count(E):
    s = E+[0]  # if s ends with '1', it requires one more "not" operation (flip), which could be easily counted by appending a '0'
    suffix_flip_cnt = [0]*len(s)
    for i in reversed(xrange(len(s)-1)):
        suffix_flip_cnt[i] = suffix_flip_cnt[i+1]+int(s[i] != s[i+1])
    return suffix_flip_cnt

def get_flip_count(suffix_flip_cnt, i):
    return suffix_flip_cnt[i] if i < len(suffix_flip_cnt) else 0

def find_X(S):
    X_cnt = [-1]*len(S)  # only valid positions with X >= 0
    X_cnt[0] = X = 0
    for i in xrange(1, len(S)):
        if S[i] == S[i-1]:
            continue
        X += 1
        X_cnt[i] = X
    return X_cnt, X+S[0]

def find_prefix_and_count(S, E, suffix_flip_cnt):
    result = float("inf")
    lookup = [-1]*(len(S))
    X_cnt, X = find_X(S)
    if 0 in [S[0], E[0]]:
        return result, X
    prefix = getPrefix(E)
    for i in xrange(2):
        j = modified_KMP(S, E, prefix, i)
        while j != -1:
            if X_cnt[-1-j] >= get_flip_count(suffix_flip_cnt, j+1):  # S[-1-j:] is the same structure as E[:j+1] and its X >= flip_cnt(E[j+1:])
                lookup[-1-j] = X_cnt[-1-j]
                result = min(result, X_cnt[-1-j]+(len(E)-(j+1)))
            j = prefix[j]
    return result, X

def double_or_noting():
    S, E = map(lambda x: [int(c) for c in list(x)], raw_input().strip().split())

    suffix_flip_cnt = init_flip_count(E)
    result, X = find_prefix_and_count(S, E, suffix_flip_cnt)
    if X >= get_flip_count(suffix_flip_cnt, 0):
        result = min(result, X+len(E))
    if E[0] == 0:
        result = min(result, X)
    else:
        cnt = get_flip_count(suffix_flip_cnt, 1)
        if cnt == 0:
            # assert(match("^10*$", E))
            result = min(result, X+1+(len(E)-1))  # S =X=> "0" =1=> "1" =(len(E)-1)=> "10*"
        elif cnt == 1:
            # assert(match("^11+0*$", E))
            result = min(result, X+1+len(E)+1)  # S =X=> "0" =1=> "1" =k=> "100+" =1=> "11+" =(len(E)-k)=> "11+0*", where 2 <= k <= len(E)
    return result if result != float("inf") else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, double_or_noting())
