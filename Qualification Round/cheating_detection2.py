# Time:  O(S * Q + SlogS + QlogQ)
# Space: O(S + Q)

def diff(players, q_ordering, i, j):
    return abs(sum(players[i][q_ordering[k]] == '0' for k in xrange(int(Q*RATIO))) -
               sum(players[j][q_ordering[k]] == '0' for k in xrange(int(Q*RATIO))) +
               sum(players[i][q_ordering[k]] == '0' for k in xrange(Q-int(Q*RATIO), Q)) -
               sum(players[j][q_ordering[k]] == '0' for k in xrange(Q-int(Q*RATIO), Q)))

def f(players, p_ordering, q_ordering, i):
    val = 0.0
    cnt = 0
    if i-1 >= 0:
        val += diff(players, q_ordering, p_ordering[i-1], p_ordering[i])
        cnt += 1
    if i+1 < S:
        val += diff(players, q_ordering, p_ordering[i], p_ordering[i+1])
        cnt += 1
    return val / cnt

def cheating_detection():
    players = []
    p_count = [0]*S
    q_count = [0]*Q
    for i in xrange(S):
        players.append(raw_input().strip())
        for j, c in enumerate(players[i]):
            if c == '0':
                continue
            p_count[i] += 1
            q_count[j] += 1
    p_ordering = range(S)
    p_ordering.sort(key=lambda x:p_count[x])
    q_ordering = range(Q)
    q_ordering.sort(key=lambda x:q_count[x])
    result = 0
    for i in xrange(S):
        if f(players, p_ordering, q_ordering, i) > f(players, p_ordering, q_ordering, result):
            result = i
    return p_ordering[result]+1

RATIO = 0.05
S, Q, T, P = 100, 10000, input(), input()
for case in xrange(T):
    print 'Case #%d: %s' % (case+1, cheating_detection())
