# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
#
# Time:  O(S * Q + SlogS + QlogQ)
# Space: O(S + Q)
#

def cheating_detection():
    scores = []
    p_count = [0]*S
    q_count = [0]*Q
    for i in xrange(S):
        scores.append(list(raw_input().strip()))
        for j, c in enumerate(scores[i]):
            if c == '0':
                continue
            p_count[i] += 1
            q_count[j] += 1
    players = sorted(range(S), key=lambda x:p_count[x])
    questions = sorted(range(Q), key=lambda x:-q_count[x])
    result, max_score = 0, 0.0
    for i in players:
        p = f = sum_f = 0.0
        for j in questions:
            if scores[i][j] == '1':
                p += 1
                sum_f += f
            else:
                f += 1
        score = (sum_f/f)*(1.0/p)
        if score > max_score:
            max_score = score
            result = i
    return result+1

S = 100
Q = 10000
T = input()
P = input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
