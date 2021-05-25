# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 2 - Problem C. Hidden Pancakes
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc20c
#
# Time:  O(N)
# Space: O(N)
#

def factorial(n):
    while len(fact) <= n:  # lazy initialization
        fact.append(fact[-1]*len(fact) % MOD)
    return fact[n]

def inverse(n):
    while len(inv) <= n:  # lazy initialization
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
    return inv[n]

def hidden_pancakes():
    N = input()
    V = map(int, raw_input().strip().split())
    V.append(1)
    result = factorial(N)  # max number of permutations
    stk = []  # keep the size of each group satisfying v
    for v in V:
        if not (v <= len(stk)+1):  # v - the number of subtrees should be less than or equal to 1
            return 0
        cnt = 0
        while v < len(stk)+1:  # pop group size and form subtrees until v == len(stk)+1
            # reresent a permutation as a tree.
            # since the total size of the current tree is cnt, for each valid permutation, it will produce cnt permutations.
            # we could inversely get the true number of valid permutations from max number of permutations.
            # so the number of permutations is as follow:
            cnt += stk.pop()
            result = (result * inverse(cnt)) % MOD
        stk.append(cnt+1)
    return result

MOD = 10**9+7
fact = [1, 1]
inv = [0, 1]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, hidden_pancakes())
