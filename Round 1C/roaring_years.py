# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem B. Roaring Years
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01
#
# Time:  O((logY)^3)
# Space: O(logY)
#

def f(x, n):
    return int("".join(str(i) for i in xrange(x, x+n)))

def binary_search(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if check(mid):
            right = mid-1
        else:
            left = mid+1
    return left

def ceil(x, n):
    return (x-1)//n+1

def min_fn(Y, n):
    y = int(Y)
    x = binary_search(1, 10**(ceil(len(Y)+1, n))-1, lambda x: f(x, n) > y)
    return f(x, n)

def roaring_years():
    Y = raw_input().strip()
    result = float("inf")
    for n in xrange(2, (len(Y)+1)+1):
        result = min(result, min_fn(Y, n))
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, roaring_years())
