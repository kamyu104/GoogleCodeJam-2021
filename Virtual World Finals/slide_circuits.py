# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals- Problem B. Slide Circuit
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084f7b2
#
# Time:  O(B + N + SlogS)
# Space: O(B + SlogS)
#
# sum of random values solution
#

from random import seed, randint
from operator import add, sub

def random_id_gen(B, ids_set):
    MAX_RAND_ID = (2**64-1)//(B*2)
    for _ in xrange(B):
        x = randint(1, MAX_RAND_ID)
        while True:
            x = randint(1, MAX_RAND_ID)
            if x not in ids_set:
                break
        ids_set.add(x)
        yield x

def get_sum(prefix, L, R, M):
    return sub(prefix[M][R//M], prefix[M][(L-1)//M])

def slide_circuits():
    B, S, N = map(int, raw_input().strip().split())
    ids_set = set()
    in_ids = [i for i in random_id_gen(B, ids_set)]
    out_ids = [i for i in random_id_gen(B,ids_set)]
    total_hash = add(reduce(add, in_ids), reduce(add, out_ids))
    slide_hashes = [0]*S
    lookup = {}
    for i in xrange(S):
        X, Y = map(int, raw_input().strip().split())
        slide_hashes[i] = add(out_ids[X-1], in_ids[Y-1])
        lookup[sub(total_hash, slide_hashes[i])] = i  # 0-indexed
    prefix = [[0] for _ in xrange(S+1)]
    for m in xrange(1, S+1):
        for i in xrange(m, S+1, m):
            prefix[m].append(add(prefix[m][-1], slide_hashes[i-1]))
    result = [0]*N
    curr_hash = total = 0
    for i in xrange(N):
        A, L, R, M = raw_input().strip().split()
        L, R, M = int(L), int(R), int(M)
        total = TOTAL_OP[A](total, R//M-(L-1)//M)
        curr_hash = HASH_OP[A](curr_hash, get_sum(prefix, L, R, M))
        result[i] = str(lookup[curr_hash]+1) if total == B-1 and curr_hash in lookup else "X"
    return " ".join(result)

seed(0)
TOTAL_OP = {'E':add, 'D':sub}
HASH_OP = {'E':add, 'D':sub}
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, slide_circuits())
