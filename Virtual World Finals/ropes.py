# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals- Problem C. ropes
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084f7b2
#
# Time:  O(N^3), pass in PyPy2 but Python2
# Space: O(N^2)
#
# Usage: python interactive_runner.py python3 testing_tool.py 2 -- python ropes.py
#

from sys import stdout, stderr

def play(i, j):
    print i+1, j+1
    stdout.flush()
    return map(lambda x: int(x)-1, raw_input().strip().split())

def check_result(A_score, B_score):
    assert(input() == int(A_score > B_score))

def greedy(score_matrix, N):
    result = None
    best_score = max(map(max, score_matrix))
    for i in xrange(2*N):
        for j in xrange(2*N):
            if score_matrix[i][j] == best_score and \
               (result is None or (sum(result) > i+j)):
               result = (i, j)
    return result

def update(score_matrix, i, j, n):
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
        i, j = greedy(score_matrix, N) if k else (Z-1, Z-1)
        A_score += score_matrix[i][j]
        update(score_matrix, i, j, N)
        i, j = play(i, j)
        B_score += score_matrix[i][j]
        update(score_matrix, i, j, N)
    check_result(A_score, B_score)

NEG_INF = float("-inf")
Z = 10  # found by experiments
T, N, W = map(int, raw_input().strip().split())
for case in xrange(T):
    ropes()
