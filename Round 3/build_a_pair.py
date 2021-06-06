# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem A. Build-A-Pair
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813aa8
#
# Time:  O((N/(2b) + 1)^b * b^2 * N), b = 10, pass in PyPy2 but Python2
# Space: O(b)
#

from operator import mul

def greedy(n, l, count, dir):  # Time: O(N)
    for i in dir(xrange(len(count))):
        if count[i] == 0:
            continue
        common = min(l, count[i])
        l -= common
        count[i] -= common
        for _ in xrange(common):
            n = 10*n + i
    return n

def odd_case(N, count):
    d = next(d for d in xrange(1, 10) if count[d])
    count[d] -= 1
    A = greedy(d, N//2, count, lambda x: x)
    B = greedy(0, N//2, count, reversed)
    return A-B

def mask_to_count(count, choice, mask):
    new_count = [0]*BASE
    for k, v in enumerate(choice):
        if not v:
            continue
        mask, cnt = divmod(mask, v)
        new_count[k] = count[k]-cnt*2
    return new_count

def even_case(count):
    choice = [0]*BASE
    for k, v in enumerate(count):
        choice[k] = v//2+1
    total = reduce(mul, (v for v in choice if v))
    result = float("inf")
    for mask in xrange(total):  # enumerate all possible prefixes
        # N/2 + b >= (c0+1) + (c1+1) + ... + (c(b-1)+1) >= b * ((c0+1)*(c1+1)*...*(c(b-1)+1))^(1/b)
        # (c0+1)*(c1+1)*...*(c(b-1)+1) <= (N/(2b) + 1)^b
        # mask loops at most O((N/(2b) + 1)^b) times
        has_prefix = True
        if count[0] and mask//count[0] == 0:  # no digit other than 0 is chosen
            if mask%count[0]:  # invalid
                continue
            has_prefix = False
        new_count = mask_to_count(count, choice, mask)
        candidates = [k for k, v in enumerate(new_count) if v and (k or has_prefix)]
        if not candidates:
            return 0
        remain = sum(new_count)
        for i in xrange(1, len(candidates)):  # O(b^2) times
            for j in xrange(i):
                tmp_count = list(new_count)
                tmp_count[candidates[i]] -= 1
                tmp_count[candidates[j]] -= 1
                A = greedy(candidates[i], remain//2-1, tmp_count, lambda x: x)  # Time: O(N)
                B = greedy(candidates[j], remain//2-1, tmp_count, reversed)  # Time: O(N)
                result = min(result, A-B)
    return result

def build_a_pair():
    D = map(int, list(raw_input().strip()))

    count = [0]*BASE
    for c in D:
        count[int(c)] += 1
    total = sum(count)
    if total%2 == 1:
        return odd_case(total, count)
    return even_case(count)

BASE = 10
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, build_a_pair())
