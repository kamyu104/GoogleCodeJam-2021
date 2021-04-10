# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1A - Problem B. Prime Time
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007543d8
#
# Time:  O((MAX_P * logX) * (M + logX)), X is the sum of all cards
# Space: O(1)
#

from collections import OrderedDict

# given prod = p1*p2*...*pk, check if
# (1) p1+p2+...+pk = total
# (2) numbers of p1,p2,...pk are within the given count limit
def check(prod, total, count):  # Time: O(M + logX)
    for p, c in count.iteritems():
        for _ in xrange(c):
            if prod%p != 0:
                break
            prod //= p  # at most O(logX) times
            total -= p
            if total < 0:
                return False
    return prod == 1 and total == 0

def prime_time():
    M = input()
    count = OrderedDict()
    for _ in xrange(M):
        P, N = map(int, raw_input().strip().split())
        count[P] = N
    X = sum(p*n for p, n in count.iteritems())

    max_card_number_of_group2 = (X-1).bit_length()  # ceil_log2_X
    max_card_sum_of_group2 = 0
    for p in reversed(count):
        max_card_sum_of_group2 += p*min(max_card_number_of_group2, count[p])
        max_card_number_of_group2 -= min(max_card_number_of_group2, count[p])
        if max_card_number_of_group2 == 0:
            break
    for i in xrange(1, max_card_sum_of_group2+1):
        if check(X-i, i, count):
            return X-i
    return 0

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, prime_time())
