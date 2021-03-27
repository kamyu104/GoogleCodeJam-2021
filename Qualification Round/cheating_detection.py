# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
#
# Time:  O(S * Q + QlogQ)
# Space: O(S + Q)
#

def cheating_detection():
    scores = []
    q_count = [0]*Q
    for i in xrange(S):
        scores.append(list(raw_input().strip()))
        for j, c in enumerate(scores[i]):
            if c == '0':
                continue
            q_count[j] += 1
    questions = sorted(range(Q), key=lambda x:q_count[x])
    result, max_score = 0, 0.0
    for i in xrange(S):
        cnt = [0]*2
        inv = 0
        for j in questions:
            if scores[i][j] == '0':
                cnt[0] += 1
                inv += cnt[1]
            else:
                cnt[1] += 1
        score = float(inv)/(1+cnt[0])/(1+cnt[1])  # count normalized inversions
        if score > max_score:  # the higher score is, the more uniform corrects is
            max_score = score
            result = i
    return result+1

S = 100
Q = 10000
T = input()
P = input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
