# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 3 - Problem B. Square Free
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436142/0000000000813aa8
#
# Time:  O(R^2 * C^2)
# Space: O(R + C)
#

def inplace_counting_sort(nums, reverse=False):  # Time: O(len(nums)), Space: O(max(nums))
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

def possible(R, C, S, D):  # Time: O(R * C), Space: O(R + C)
    inplace_counting_sort(S, reverse=True)
    inplace_counting_sort(D, reverse=True)
    S_prefix = [0]
    for i in xrange(len(S)):
        S_prefix.append(S_prefix[-1] + S[i])
    D_suffix = [0]
    for i in reversed(xrange(len(D))):
        D_suffix.append(D_suffix[-1] + D[i])
    D_suffix.reverse()
    return all(S_prefix[(i-1)+1]-D_suffix[j] <= i*j for i in xrange(R) for j in xrange(C))

def square_free():
    R, C = map(int, raw_input().strip().split())
    S = map(lambda x: C-int(x), raw_input().strip().split())
    D = map(lambda x: R-int(x), raw_input().strip().split())

    if sum(S) != sum(D) or not possible(R, C, S[:], D[:]):
        return "IMPOSSIBLE"
    result = [['/' for _ in xrange(C)] for _ in xrange(R)]
    for i in xrange(R):
        for j in xrange(C):
            if not (S[i] >= 1 and D[j] >= 1 and possible(R, C, [S[k]-int(k == i) for k in xrange(len(S))], [D[k]-int(k == j) for k in xrange(len(D))])):
                continue
            result[i][j] = '\\'
            S[i], D[j] = S[i]-1, D[j]-1
    return "POSSIBLE\n"+"\n".join("".join(row) for row in result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, square_free())
