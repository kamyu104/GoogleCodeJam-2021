# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals - Problem A. Cutting Cake
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084fba1
#
# Time:  O(NlogN)
# Space: O(N)
#

from fractions import Fraction

def ccw(A, B, C):
    return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])

def find_delta_slopes(points):
    delta_slopes = [Fraction(0)]*3
    for i in xrange(len(points)):
        if not points[i][0]-points[i-1][0]:
            continue
        slope = Fraction(points[i][1]-points[i-1][1], points[i][0]-points[i-1][0])
        delta_slopes[i-1] += slope
        delta_slopes[i] -= slope
    assert(sum(delta_slopes) == 0)
    return delta_slopes

def cutting_cake():
    N, W, H = map(int, raw_input().strip().split())
    P, Q, R, S = map(Fraction, raw_input().strip().split())
    points = sorted([(Fraction(0), Fraction(0)), (P, Q), (R, S)])
    prev_diff, area = Fraction(0), Fraction(-ccw(*points), 2)
    events = []
    for _ in xrange(N):
        X, Y, A, B = map(Fraction, raw_input().strip().split())
        prev_diff -= B*area
        for i in xrange(len(points)):
            events.append((X+points[i][0], i, A+B))
    events.sort()

    result = abs(prev_diff)
    delta_y = [points[i][1]-points[i-1][1] if points[i-1][0] == points[i][0] else 0 for i in xrange(len(points))]
    delta_slopes = find_delta_slopes(points)
    prev_x = prev_y = slope = Fraction(0)
    for curr_x, i, w in events:
        dx = curr_x-prev_x
        if not dx:
            prev_y += w*delta_y[i]
            slope += w*delta_slopes[i]
            continue
        curr_y = prev_y+dx*slope
        curr_diff = prev_diff+(prev_y+curr_y)/2*dx
        result = min(result, abs(curr_diff))  # the values at each endpoint of the interval
        extreme_diff = prev_diff
        if curr_y*prev_y < 0:  # find the value at the extreme point of the quadratic if that's within the interval
            extreme_y = Fraction(0)
            extreme_x = (extreme_y-prev_y)/slope+prev_x
            extreme_diff = prev_diff+(prev_y+extreme_y)/2*(extreme_x-prev_x)
            result = min(result, abs(extreme_diff))
        if min(extreme_diff, prev_diff, curr_diff) <= 0 <= max(extreme_diff, prev_diff, curr_diff):  # whether the quadratic crosses 0 within the interval
            result = Fraction(0)
            break
        prev_diff, prev_x, prev_y = curr_diff, curr_x, curr_y
        slope += w*delta_slopes[i]
    result /= abs(area)
    return "%s/%s"%(result.numerator, result.denominator)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, cutting_cake())
