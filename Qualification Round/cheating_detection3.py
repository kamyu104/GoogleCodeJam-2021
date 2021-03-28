# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
#
# Time:  O(S * Q + SlogS + QlogQ)
# Space: O(S + Q)
#

from math import exp

def f(x):
    return 1.0/(1.0+exp(-x))

def cheating_detection():
    scores = []
    p_count = [0]*S
    q_count = [0]*Q
    for i in xrange(S):
        scores.append(raw_input().strip())
        for j, c in enumerate(scores[i]):
            if c == '0':
                continue
            p_count[i] += 1
            q_count[j] += 1
    players = sorted(range(S), key=lambda x:p_count[x])
    questions = sorted(range(Q), key=lambda x:q_count[x])
    result = 0
    si = MIN
    max_diff = 0.0
    result = -1
    for i in players:
        qj = MAX
        diff = 0.0
        for j in questions:
            diff += (int(scores[i][j] == '1')-f(si-qj))**2
            qj -= Q_D
        diff /= (1+p_count[i])*(1+(Q-p_count[i]))  # normalize diff by weakness and strength, both ends are divided less and the middle are divided more
        if diff > max_diff:
            max_diff = diff
            result = i
        si += S_D
    return result+1

MIN, MAX = -3.0, 3.0
S, Q, = 100, 10000
S_D, Q_D = (MAX-MIN)/S, (MAX-MIN)/Q
T, P = input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
