# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 2 - Problem A. Minimum Sort
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435915/00000000007dc51c
#
# Time:  O(N * Q), Q is the time of query_minimum
# Space: O(1)
#
# Usage: python interactive_runner.py python3 testing_tool.py -- python minimum_sort.py
#

from sys import stdout

def query(i, j):
    print "M %s %s" % (i, j)
    stdout.flush()
    return input()

def swap(i, j):
    print "S %s %s" % (i, j)
    stdout.flush()
    return input()

def done():
    print "D"
    stdout.flush()
    return input()

def minimum_sort():
    for i in xrange(1, N):
        idx = query(i, N)
        if idx != i:
            swap(i, idx)
    if done() != 1:
        exit()
        
T, N = map(int, raw_input().strip().split())
for case in xrange(T):
    minimum_sort()
