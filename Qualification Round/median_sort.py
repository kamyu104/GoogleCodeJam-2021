# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Qualification Round - Problem D. Median Sort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1284
#
# Time:  O(N^2)
# Space: O(1)
# Usage: python interactive_runner.py python3 testing_tool.py 2 -- python median_sort.py
#

from sys import stdout

def query(i, j, k):
    print i, j, k
    stdout.flush()
    return input()

def check(result):
    print " ".join(map(str, result))
    stdout.flush()
    ok = raw_input().strip()
    if ok != "1":  # error
        exit()

def median_sort():
    result = [1, 2]
    for i in xrange(3, N+1):  # Time: O(N)
        left, right = 0, len(result)-1
        while left < right:  # Time: O(logN)
            m1 = left + (right-left)//3
            m3 = right - (right-left)//3
            x = query(result[m1], result[m3], i)
            if x == result[m1]:
                right = m1-1
                if left == right:
                    right += 1
            elif x == result[m3]:
                left = m3+1
                if left == right:
                    left -= 1
            else:
                left, right = m1+1, m3-1
                if left == right:
                    right += 1                
        result.insert(left, i)  # Time: O(N)
    check(result)

T, N, Q = map(int, raw_input().strip().split())
for case in xrange(T):
    median_sort()
