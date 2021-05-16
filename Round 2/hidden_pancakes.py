# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 2 - Problem C. Hidden Pancakes
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc20c
#
# Time:  O(N)
# Space: O(N)
#

def factorial(n):
    while len(inv) <= n:  # lazy initialization
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)  # https://cp-algorithms.com/algebra/module-inverse.html
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return fact[n]

def hidden_pancakes():
    N = input()
    V = map(int, raw_input().strip().split())
    V.append(1)
    result = factorial(N)
    stk = []
    for v in V:
        if not (v <= len(stk)+1):
            return 0
        cnt = 0
        while v < len(stk)+1:
            cnt += stk.pop()
            result = (result * inv[cnt]) % MOD
        stk.append(cnt+1)
    return result

MOD = 10**9+7
fact = [1, 1]
inv = [0, 1]
inv_fact = [1, 1]    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, hidden_pancakes())
