# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
#
# Time:  O(S * Q)
# Space: O(S + Q)
#

def normalized(a):
    total = float(sum(a))/len(a)
    for i in xrange(len(a)):
        a[i] -= total

def covariance(a, b):
    return sum(a[i]*b[i] for i in xrange(len(a)))

def correlation(a, b):
    return covariance(a, b) / covariance(a, a)**0.5 / covariance(b, b)**0.5

def cheating_detection():
    scores = []
    q_count = [0]*Q
    for i in xrange(S):
        scores.append(map(int, list(raw_input().strip())))
        for j, c in enumerate(scores[i]):
            if not c:
                continue
            q_count[j] += 1
    normalized(q_count)
    result, min_corr = 0, 1.0
    for i, score in enumerate(scores):
        normalized(score)
        corr = correlation(score, q_count)
        if corr < min_corr:
            min_corr = corr
            result = i
    return result+1

S, Q, T, P = 100, 10000, input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
