# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
#
# Time:  O(S * Q + SlogS + QlogQ)
# Space: O(S + Q)
#
# Difference with expected distribution method
# Accuracy: 1000/1000 = 100.0%
#

from math import exp

def f(x):
    return 1.0/(1.0+exp(-x))

def cheating_detection():
    scores = []
    p_count = [0]*S
    q_count = [0]*Q
    for i in xrange(S):
        scores.append(map(int, list(raw_input().strip())))
        for j, c in enumerate(scores[i]):
            p_count[i] += c
            q_count[j] += c
    players = sorted(range(S), key=lambda x:p_count[x])
    questions = sorted(range(Q), key=lambda x:q_count[x])
    si = MIN
    result, max_score, si = 0, 0.0, MIN
    for i in players:
        score, qj = 0.0, MAX
        for j in questions:
            score += (scores[i][j]-f(si-qj))**2
            qj -= Q_D
        score /= (1+p_count[i])*(1+(Q-p_count[i]))  # normalize score by weakness and strength, both ends are divided less and the middle are divided more
        if score > max_score:
            max_score = score
            result = i
        si += S_D
    return result+1

MIN, MAX = -3.0, 3.0
S, Q, = 100, 10000
S_D, Q_D = (MAX-MIN)/S, (MAX-MIN)/Q
T, P = input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
