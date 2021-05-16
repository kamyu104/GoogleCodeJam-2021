# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 2 - Problem C. Hidden Pancakes
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc20c
#
# Time:  precompute: O(N)
#        runtime:    O(N)
# Space: O(N)
#

def nCr(n, k):
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def hidden_pancakes():
    N = input()
    V = map(int, raw_input().strip().split())
    V.append(1)
    result = 1
    stk = []
    for v in V:
        if v > len(stk)+1:
            return 0
        cnt = 0
        while len(stk) >= v:
            result = result * nCr(stk[-1]+cnt, cnt) % MOD
            cnt += stk[-1]+1
            stk.pop()
        stk.append(cnt)
    return result

MOD = 10**9+7
MAX_N = 10**5
fact = [0]*(MAX_N+1)
inv = [0]*(MAX_N+1)
inv_fact = [0]*(MAX_N+1)
fact[0] = inv_fact[0] = fact[1] = inv_fact[1] = inv[1] = 1
for i in xrange(2, len(fact)):
    fact[i] = fact[i-1]*i % MOD
    inv[i] = inv[MOD%i]*(MOD-MOD//i) % MOD  # https://cp-algorithms.com/algebra/module-inverse.html
    inv_fact[i] = inv_fact[i-1]*inv[i] % MOD
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, hidden_pancakes())
