# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 2 - Problem C. Hidden Pancakes
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc20c
#
# Time:  O(N)
# Space: O(N)
#

def nCr(n, k):
    while len(inv) <= n:  # lazy initialization
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def hidden_pancakes():
    N = input()
    V = map(int, raw_input().strip().split())
    V.append(1)
    result = 1
    stk = []  # keep the size of each group satisfying v
    for v in V:
        if not (v <= len(stk)+1):  # v - the number of subtrees should be less than or equal to 1
            return 0
        cnt = 0
        while v < len(stk)+1:  # pop group size and form subtrees until v == len(stk)+1
            # reresent a permutation as a tree,
            # use the largest pancake of the group as root,
            # and the size of left subtree is stk[-1]-1, the size of right subtree is cnt.
            # so the number of permutations is as follow:
            result = result * nCr(cnt+(stk[-1]-1), (stk[-1]-1)) % MOD
            cnt += stk.pop()
        stk.append(cnt+1)  # len(stk) == v
    return result

MOD = 10**9+7
fact = [1, 1]
inv = [0, 1]
inv_fact = [1, 1]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, hidden_pancakes())