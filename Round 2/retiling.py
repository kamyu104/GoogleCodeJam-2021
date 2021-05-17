# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 2 - Problem D. Retiling
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc2de
#
# Time:  O((R * C)^3)
# Space: O((R * C)^2)
#

# Template translated from:
# https://github.com/kth-competitive-programming/kactl/blob/main/content/graph/WeightedMatching.h
# Time:  O(N^2 * M)
# Space: O(N + M)
def hungarian(a):
    if not a:
        return 0, []
    n, m = len(a)+1, len(a[0])+1
    u, v, p, ans = [0]*n, [0]*m, [0]*m, [0]*(n-1)
    for i in xrange(1, n):
        p[0] = i
        j0 = 0  # add "dummy" worker 0
        dist, pre = [float("inf")]*m, [-1]*m
        done = [False]*(m+1)
        while True:  # dijkstra
            done[j0] = True
            i0, j1, delta = p[j0], None, float("inf")
            for j in xrange(1, m):
                if done[j]:
                    continue
                cur = a[i0-1][j-1]-u[i0]-v[j]
                if cur < dist[j]:
                    dist[j], pre[j] = cur, j0
                if dist[j] < delta:
                    delta, j1 = dist[j], j
            for j in xrange(m):
                if done[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    dist[j] -= delta
            j0 = j1
            if not p[j0]:
                break
        while j0:  # update alternating path
            j1 = pre[j0]
            p[j0], j0 = p[j1], j1
    for j in xrange(1, m):
        if p[j]:
            ans[p[j]-1] = j-1
    return -v[0], ans  # min cost

def retiling():
    R, C, F, S = map(int, raw_input().strip().split())
    src, dst = [[list(raw_input().strip()) for _ in xrange(R)] for _ in xrange(2)]
    loc0 = [(i, j) for i in xrange(R) for j in xrange(C) if src[i][j] == 'M']
    loc1 = [(i, j) for i in xrange(R) for j in xrange(C) if dst[i][j] == 'M']
    cost = [[0]*(len(loc0)+len(loc1)) for _ in xrange(len(loc0)+len(loc1))]
    for i in xrange(len(cost)):
        for j in xrange(len(cost[0])):
            if i < len(loc0) and j < len(loc1):
                cost[i][j] = S * (abs(loc0[i][0]-loc1[j][0])+abs(loc0[i][1]-loc1[j][1]))
            elif i < len(loc0) or j < len(loc1):
                cost[i][j] = F
    return hungarian(cost)[0]

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, retiling())
