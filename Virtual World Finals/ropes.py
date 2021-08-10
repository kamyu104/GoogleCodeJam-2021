# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals- Problem C. Ropes
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084fad0
#
# Time:  O(N^3), pass in PyPy2 but Python2
# Space: O(N^2)
#
# Usage: python interactive_runner.py python3 testing_tool.py 2 -- python ropes.py
#
# push it east solution
#   - Z=10, 18322/20000 = 91.610 %
#   - Z=14, 18251/20000 = 91.255 %
#

from sys import stdout
from itertools import imap

def play(i, j):
    print i+1, j+1  # 0-indexed
    stdout.flush()
    return map(lambda x: int(x)-1, raw_input().strip().split())  # 0-indexed

def check_result(A_score, B_score):
    assert(input() == int(A_score > B_score))

def greedy(score_matrix):
    # given that opposing team choose the play that yields the maximum possible score for this turn.
    # if there is a tie:
    #   - they will choose one at random as problem description claims
    #   - they will not choose by a counter-greedy strategy (they choose as far east as possible), since we can never win by this greedy strategy if they can always do that
    result = None
    best_score = max(imap(max, score_matrix))
    for i in xrange(2*N):
        for j in xrange(2*N):
            if score_matrix[i][j] == best_score and (result is None or (sum(result) > i+j)):  # we choose as far west as possible if there is a tie
               result = (i, j)
    return result

def update(i, j, score_matrix):
  for r in xrange(2*N):
      for c in xrange(2*N):
          if r == i or c == j:
              score_matrix[r][c] = NEG_INF
          elif (r-i)*(c-j) < 0:
              score_matrix[r][c] += 1

def ropes():
    score_matrix = [[0 for _ in xrange(2*N)] for _ in xrange(2*N)]
    A_score = B_score = 0
    for k in xrange(N):
        i, j = greedy(score_matrix) if k else (Z-1, Z-1)  # tuned by experitments that i=j at the first play is better
        A_score += score_matrix[i][j]
        update(i, j, score_matrix)
        i, j = play(i, j)
        B_score += score_matrix[i][j]
        update(i, j, score_matrix)
    check_result(A_score, B_score)

NEG_INF = float("-inf")
Z = 10  # tuned by experiments that top 4 win rates are with Z = [10, 14, 9, 11]
T, N, W = map(int, raw_input().strip().split())
for case in xrange(T):
    ropes()
