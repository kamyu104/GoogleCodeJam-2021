# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem B. Square Free
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813e1a
#
# Time:  O(R^2 * C^2)
# Space: O(R + C)
#

def inplace_counting_sort(nums, reverse=False):  # Time: O(len(nums)+max(nums)), Space: O(max(nums))
    count = [0]*(max(nums)+1)
    for num in nums:
        count[num] += 1
    for i in xrange(1, len(count)):
        count[i] += count[i-1]
    for i in reversed(xrange(len(nums))):  # inplace but unstable sort
        if nums[i] < 0:  # processed
            continue
        while i != count[nums[i]]-1:
            count[nums[i]] -= 1
            nums[count[nums[i]]], nums[i] = ~nums[i], nums[count[nums[i]]]
        count[nums[i]] -= 1
        nums[i] = ~nums[i]
    for i in xrange(len(nums)):
        nums[i] = ~nums[i]  # restore values
    if reverse:  # unstable sort
        nums.reverse()

def possible(S, D):  # Time: O(R * C), Space: O(R + C)
    inplace_counting_sort(S, reverse=True)  # Time: O(R + C), Space: O(C)
    inplace_counting_sort(D, reverse=True)  # Time: O(R + C), Space: O(R)
    S_prefix = [0]
    for i in xrange(len(S)):  # Time: O(R), Space: O(R)
        S_prefix.append(S_prefix[-1] + S[i])
    D_suffix = [0]
    for i in reversed(xrange(len(D))):  # Time: O(C), Space: O(C)
        D_suffix.append(D_suffix[-1] + D[i])
    D_suffix.reverse()
    # consider a graph running max flow algorithm where edge from source to each Sx is with weight S[x], edge from each Sx to each Dy is with weight 1, edge from each Dy to sink is with weight D[y],
    # if sum(S) != sum(D), it is impossible,
    # otherwise, we want all nodes with full capacity,
    # it is possible
    # <=> sum(S[x] for x in X)-sum(D[y] for y in Y) <= |X|*(C-|Y|) for all 0 <= |X| <= R and 0 <= |Y| <= C
    # <=> sum(S[x] for x in X')-sum(D[y] for y in Y') <= |X|*|Y| for all 0 <= |X| <= R and 0 <= |Y| <= C
    #     and X'  is the biggist |X| of S and Y'  is the smallest C-|Y| of D
    # <=> -(sum(S)-sum(S[x] for x in X'))+(sum(D)-sum(D[y]) for y in Y') <= |X|*|Y| for all 0 <= |X| <= R and 0 <= |Y| <= C
    #     and X'  is the biggist |X| of S and Y'  is the smallest C-|Y| of D
    # <=> sum(D[y] for y in Y'')-sum(S[x] for x in X'') <= |X|*|Y| for all 0 <= |X| <= R and 0 <= |Y| <= C
    #     and Y'' is the biggest |Y| of D and X'' is the smallest R-|X| of S
    return S_prefix[-1] == D_suffix[0] and \
           all(S_prefix[i]-D_suffix[j] <= i*j for i in xrange(len(S_prefix)) for j in xrange(len(D_suffix)))  # Time: O(R * C)

def square_free():
    R, C = map(int, raw_input().strip().split())
    S = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())

    if not possible(S[:], D[:]):
        return "IMPOSSIBLE"
    result = [['\\']*C for _ in xrange(R)]
    for i in reversed(xrange(R)):
        for j in xrange(C):
            if not (S[i] >= 1 and D[j] >= 1 and possible([S[k]-int(k == i) for k in xrange(len(S))], [D[k]-int(k == j) for k in xrange(len(D))])):
                continue
            result[i][j] = '/'
            S[i], D[j] = S[i]-1, D[j]-1
    return "POSSIBLE\n"+"\n".join("".join(row) for row in result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, square_free())
