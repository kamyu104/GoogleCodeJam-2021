# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1C - Problem B. Roaring Years
# https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01
#
# Time:  O(D^2 * logD), D is the digit count of Y, since sum((D/n)*D for n in [2, D+1]) = D^2 * O(logD)
# Space: O(D)
#

def ceil(x, n):
    return (x-1)//n+1

def floor(x, n):
    return x//n

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

def min_fn(Y, n):
    y = int(Y)
    # find any x, s.t. f(x, n) > y
    # => X = str(x), f(x, n) > X*n >= 10**len(Y) > y
    # => len(X)*n >= len(Y)+1
    # => len(X) = ceil(len(Y)+1, n)
    # => x is in the range [10**(ceil(len(Y)+1, n)-1), 10**ceil(len(Y)+1, n)-1]
    # => let right be 10**(ceil(len(Y)+1, n)-1)
    right = 10**(ceil(len(Y)+1, n)-1)
    assert(f(right, n) > y)
    # find any x, s.t. f(x, n) <= y
    # => X = str(x), f(x, n) < X*n <= 10**(len(Y)-1) <= y
    # => len(X)*n <= len(Y)
    # => len(X) = floor(len(Y), n)
    # => x is in the range [1, 10**(floor(len(Y), n)-1)-n+1]
    # => let left be max(1, 10**(floor(len(Y), n)-1)-n+1)
    left = max(1, 10**(floor(len(Y), n)-1)-n+1)
    x = binary_search(left, right, lambda x: f(x, n) > y)  # find the smallest x, s.t. f(x, n) > y
    return f(x, n)

def roaring_years():
    Y = raw_input().strip()
    return min(min_fn(Y, n) for n in xrange(2, (len(Y)+1)+1))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, roaring_years())
