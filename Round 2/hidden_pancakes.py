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
    V.append(1)  # add a virtual value to count the permutation of remaining subtrees
    result = 1
    stk = []  # keep the size of each subtree satisfying v
    for v in V:
        if not (v <= len(stk)+1):  # v minus the number of subtrees should be less than or equal to 1
            return 0
        cnt = 0
        while v < len(stk)+1:  # pop subtree size and form a new tree until the number of subtrees on stack is v
            # a tree structure is constructed by v, count the valid permutations:
            # the largest pancake size of each subtee on stack keeps monotonically decreasing.
            # to merge the subtree on the top of stack, use its largest pancake as root of a new tree,
            # the rest part of the subtree is as a subtree with size stk[-1]-1,
            # and the previously merged subtree is as a subtree with size cnt.
            # so the number of valid permutations is as follows:
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