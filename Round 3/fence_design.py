# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem C. Fence Design
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813bc7
#
# Time:  O(NlogN) on average, pass in PyPy2 but Python2
# Space: O(N)
#

from random import seed, randint

# Compute the cross product of vectors AB and AC
CW, COLLINEAR, CCW = range(-1, 2)
def ccw(A, B, C):
    area = (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
    return CCW if area > 0 else CW if area < 0 else COLLINEAR

def same_side(A, B, C, D):
    return ccw(A,C,D) == 0 or ccw(B,C,D) == 0 or ccw(A,C,D) == ccw(B,C,D)

def rotate(hull, split):
    for i in xrange(len(hull)):
        if hull[i] in split and hull[(i-1)%len(hull)] in split:
            return hull[i:]+hull[:i]
    return hull[:]

def add_result(result, x):
    result.add(tuple(sorted(x)))

def add_triangle(P, left_ccw, right_cw, result, lookup):
    p, q = 0, 1
    while True:
        p1 = (p+1)%len(left_ccw)
        if ccw(P[left_ccw[p1]], P[left_ccw[p]], P[right_cw[q]]) > 0:
            add_result(result, [left_ccw[p1], right_cw[q]])
            lookup.add(left_ccw[p])  # inside the convex hull
            p = p1
            continue
        q1 = (q+1)%len(right_cw)
        if ccw(P[left_ccw[p]], P[right_cw[q]], P[right_cw[q1]]) > 0:
            add_result(result, [right_cw[q1], left_ccw[p]])
            lookup.add(right_cw[q])  # inside the convex hull
            q = q1
            continue
        break

def conquer(P, left, right, split, result):  # Time: O(N)
    if len(left) == 2:
        return right
    if len(right) == 2:
        return left
    lookup = set()
    left_ccw, right_cw = rotate(left, split), rotate(right[::-1], split)
    add_triangle(P, left_ccw, right_cw, result, lookup)
    right_ccw, left_cw = rotate(right, split), rotate(left[::-1], split)
    add_triangle(P, right_ccw, left_cw, result, lookup)
    hull = [x for x in left_ccw if x not in lookup] + \
           [x for x in right_ccw[1:-1] if x not in lookup]
    points = set(x for x in left_ccw).union(set(x for x in right_ccw))
    points = [P[x] for x in points]
    return hull

def divide(P, f, curr, split, result):  # depth at most O(logN) on average => Time: O(NlogN)
    if len(curr) == 2:
        return curr
    if len(curr) == 3:  # special case since random pick may fail to split
        p = next(p for p in curr if p not in split)
        for x in split:
            add_result(result, [p, x])
        return [p, split[0], split[1]] if ccw(P[p], P[split[0]], P[split[1]]) > 0 else [p, split[1], split[0]]
    if f:  # prefer to use pre-placed fence
        new_split = f.pop()
    else:
        while True:
            idx = randint(0, len(curr)-1)
            p = curr[idx]
            curr[idx], curr[-1] = curr[-1], curr[idx]
            q = curr[randint(0, len(curr)-2)]
            if p > q:
                p, q = q, p
            if (p, q) not in result:
                break
        new_split = (p, q)
    add_result(result, new_split)
    left = [x for x in curr if ccw(P[new_split[0]], P[new_split[1]], P[x]) >= 0]
    right = [x for x in curr if ccw(P[new_split[0]], P[new_split[1]], P[x]) <= 0]
    return conquer(P,
                   divide(P, f if f and f[-1][0] in left and f[-1][1] in left else [], left, new_split, result),
                   divide(P, f if f and f[-1][0] in right and f[-1][1] in right else [], right, new_split, result),
                   new_split, result)

def fence_design():
    N = input()
    P = [map(int, raw_input().strip().split()) for _ in xrange(N)]
    f = [map(lambda x:int(x)-1, raw_input().strip().split()) for _ in xrange(2)]
    f = [tuple(sorted(x)) for x in f]

    if same_side(P[f[1][0]], P[f[1][1]], P[f[0][0]], P[f[0][1]]):
        # f[0] won't be intersected by the other, it should be splitted later,
        # f[1] may be intersected by the other f, it should be splitted first, and it doesn't intersect f[0] while splitting
        f[0], f[1] = f[1], f[0]
    result = set()
    divide(P, f[:], range(len(P)), [], result)
    return "%s\n"%(len(result)-2)+"\n".join("%s %s"%(x[0]+1, x[1]+1) for x in [x for x in result if x not in f])

seed(0)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fence_design())
