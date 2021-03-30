# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
#
# Time:  O(S * Q + SlogS + QlogQ)
# Space: O(S + Q)
#
# Difference with neighbors in easiest and hardest 5% questions method
# Accuracy: 982/1000 = 98.2%
#

def diff(player1, player2, extreme_questions):
    return abs(sum(player1[j] for j in extreme_questions) - sum(player2[j] for j in extreme_questions))

def neighbor_diffs(scores, players, extreme_questions, i):
    diffs = cnt = 0
    if i-1 >= 0:
        diffs += diff(scores[players[i-1]], scores[players[i]], extreme_questions)
        cnt += 1
    if i+1 < S:
        diffs += diff(scores[players[i]], scores[players[i+1]], extreme_questions)
        cnt += 1
    return float(diffs)/cnt

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
    extreme_questions = [questions[j] for j in xrange(int(Q*EXTREME_RATIO))] + [questions[j] for j in xrange(Q-int(Q*EXTREME_RATIO), Q)]
    result = 0
    for i in xrange(S):
        if neighbor_diffs(scores, players, extreme_questions, i) > neighbor_diffs(scores, players, extreme_questions, result):
            result = i
    return players[result]+1

EXTREME_RATIO = 0.05
S, Q, T, P = 100, 10000, input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
