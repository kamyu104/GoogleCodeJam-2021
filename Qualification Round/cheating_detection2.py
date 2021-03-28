# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1155
#
# Time:  O(S * Q + SlogS + QlogQ)
# Space: O(S + Q)
#

def diff(player1, player2, extreme_questions):
    return abs(sum(player1[j] == '1' for j in extreme_questions) - sum(player2[j] == '1' for j in extreme_questions))

def neighbor_diffs(scores, players, extreme_questions, i):
    val = 0.0
    cnt = 0
    if i-1 >= 0:
        val += diff(scores[players[i-1]], scores[players[i]], extreme_questions)
        cnt += 1
    if i+1 < S:
        val += diff(scores[players[i]], scores[players[i+1]], extreme_questions)
        cnt += 1
    return val / cnt

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
