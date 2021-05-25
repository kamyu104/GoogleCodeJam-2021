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
    V.append(1)  # add a virtual value to count the permutation of remaining subtrees
    result = factorial(N)  # max number of permutations
    stk = []  # keep the size of each subtree satisfying v
    for v in V:
        if not (v <= len(stk)+1):  # v minus the number of subtrees should be less than or equal to 1
            return 0
        cnt = 0
        while v < len(stk)+1:  # pop subtree size and form a new tree until the number of subtrees on stack is v
            # a tree structure is formed by v, count the valid permutations:
            # the size of the largest pancake of each subtee on stack keeps monotonically decreasing.
            # since the total size of the current merged tree is cnt, we can only choose the largest pancake as root from cnt pancakes.
            # thus we could inversely get the true number of valid permutations from max number of permutations.
            # so the number of valid permutations is as follows:
            cnt += stk.pop()
            result = (result * inverse(cnt)) % MOD
        stk.append(cnt+1)  # len(stk) == v
    return result

MOD = 10**9+7
fact = [1, 1]
inv = [0, 1]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, hidden_pancakes())
