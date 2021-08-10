# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals- Problem B. Slide Circuits
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
    MAX_RAND_ID = MAX_UINT64//(B*2)
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
    out_ids = [i for i in random_id_gen(B, ids_set)]
    total_hash = add(reduce(add, in_ids), reduce(add, out_ids))
    slide_hashes = [0]*S
    lookup = {}
    for i in xrange(S):
        X, Y = map(int, raw_input().strip().split())
        slide_hashes[i] = add(out_ids[X-1], in_ids[Y-1])
        lookup[sub(total_hash, slide_hashes[i])] = i  # 0-indexed
    prefix = [[0] for _ in xrange(S+1)]
    for m in xrange(1, S+1):  # sum of harmonic series: O(S/1 + S/2 + ... + S/S) = O(S * (1 + 1/2 + ... + 1/S)) = O(SlogS)
        for i in xrange(m, S+1, m):
            prefix[m].append(add(prefix[m][-1], slide_hashes[i-1]))
    result = [0]*N
    curr_hash = 0
    for i in xrange(N):
        A, L, R, M = raw_input().strip().split()
        L, R, M = int(L), int(R), int(M)
        curr_hash = HASH_OP[A](curr_hash, get_sum(prefix, L, R, M))
        if curr_hash in lookup:
            result[i] = lookup[curr_hash]+1
    return " ".join(map(lambda x: str(x) if x else "X", result))

seed(0)
MAX_UINT64 = 2**64-1
HASH_OP = {'E':add, 'D':sub}
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, slide_circuits())
