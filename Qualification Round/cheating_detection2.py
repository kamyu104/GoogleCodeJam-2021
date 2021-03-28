# Time:  O(S * Q + SlogS + QlogQ)
# Space: O(S + Q)

def diff(player1, player2, questions):
    return abs(sum(player1[questions[i]] == '1' for i in xrange(int(Q*RATIO))) -
               sum(player2[questions[i]] == '1' for i in xrange(int(Q*RATIO))) +
               sum(player1[questions[i]] == '1' for i in xrange(Q-int(Q*RATIO), Q)) -
               sum(player2[questions[i]] == '1' for i in xrange(Q-int(Q*RATIO), Q)))

def f(scores, players, questions, i):
    val = 0.0
    cnt = 0
    if i-1 >= 0:
        val += diff(scores[players[i-1]], scores[players[i]], questions)
        cnt += 1
    if i+1 < S:
        val += diff(scores[players[i]], scores[players[i+1]], questions)
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
    result = 0
    for i in xrange(S):
        if f(scores, players, questions, i) > f(scores, players, questions, result):
            result = i
    return players[result]+1

RATIO = 0.05
S, Q, T, P = 100, 10000, input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
