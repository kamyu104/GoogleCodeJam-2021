# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem A. Build-A-Pair
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813aa8
#
# Time:  O(3^b * b * N), b = 10, pass in PyPy2 but Python2
# Space: O(b)
#
# optimized from build_a_pair.py
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

def odd_case(N, count):  # Time: O(N)
    d = next(d for d in xrange(1, len(count)) if count[d])
    count[d] -= 1
    A = greedy(d, N//2, count, lambda x: x)
    B = greedy(0, N//2, count, reversed)
    return A-B

def mask_to_count(count, choice, mask):  # Time: O(b)
    new_count = [0]*BASE
    for k, v in enumerate(choice):
        mask, cnt = divmod(mask, v)
        new_count[k] = cnt*2+count[k]%2 if cnt != CHOICE-1 else count[k]
    return new_count

def even_case(count):  # Time: O(3^b * b * N)
    choice = [0]*BASE
    for k, v in enumerate(count):
        choice[k] = min(v//2+1, CHOICE)
    total = reduce(mul, (v for v in choice if v))
    result = float("inf")
    for mask in xrange(total):  # enumerate all possible prefixes, loops O(3^b) times
        has_prefix = True
        new_count = mask_to_count(count, choice, mask)
        if all(new_count[k] == count[k] for k in xrange(1, len(count))):  # no digit other than 0 is chosen
            if new_count[0] != count[0]:  # invalid
                continue
            has_prefix = False
        candidates = [k for k, v in enumerate(new_count) if v and (k or has_prefix)]
        if not candidates:
            return 0
        if len(candidates) == 1:
            continue
        remain = sum(new_count)
        min_diff = min(candidates[i]-candidates[i-1] for i in xrange(1, len(candidates)))
        for i in xrange(1, len(candidates)):  # O(b) times
            a, b = candidates[i], candidates[i-1]
            if new_count[b] == 0 or a-b != min_diff:  # for each a, b s.t. a-b > min_diff, which A-B won't be the result
                continue
            tmp_count = list(new_count)
            tmp_count[a] -= 1
            tmp_count[b] -= 1
            A = greedy(a, remain//2-1, tmp_count, lambda x: x)  # Time: O(N)
            B = greedy(b, remain//2-1, tmp_count, reversed)  # Time: O(N)
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

CHOICE = 3  # other than the shared prefix, since keeping 1 pair may happen in some cases, for each digit, we have 3 choices to keep: 0 pair, 1 pair, all pairs
BASE = 10
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, build_a_pair())
