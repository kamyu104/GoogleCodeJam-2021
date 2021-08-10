# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals- Problem B. Slide Circuit
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084f7b2
#
# Time:  O(B + N + SlogS)
# Space: O(B + SlogS)
#
# polynomial hashes solution (slower)
#

def poly_hash_id_gen(B, basis):
    for _ in xrange(B):
        yield basis[0]
        basis[0] = (basis[0]*p)%MOD

def get_sum(prefix, L, R, M):
    return sub(prefix[M][R//M], prefix[M][(L-1)//M])

def slide_circuits():
    B, S, N = map(int, raw_input().strip().split())
    basis = [1]
    in_ids = [i for i in poly_hash_id_gen(B, basis)]
    out_ids = [i for i in poly_hash_id_gen(B, basis)]
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
    total = curr_hash = 0
    for i in xrange(N):
        A, L, R, M = raw_input().strip().split()
        L, R, M = int(L), int(R), int(M)
        total = TOTAL_OP[A](total, R//M-(L-1)//M)
        curr_hash = HASH_OP[A](curr_hash, get_sum(prefix, L, R, M))
        if total == B-1 and curr_hash in lookup:
            result[i] = lookup[curr_hash]+1
    return " ".join(map(lambda x: str(x) if x else "X", result))

MOD, p = 2**64-59, 113  # MOD is max 64-bit prime
add = lambda a, b: (a+b)%MOD
sub = lambda a, b: (a-b)%MOD
TOTAL_OP = {'E':lambda a,b: a+b, 'D':lambda a, b:a-b}
HASH_OP = {'E':add, 'D':sub}
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, slide_circuits())
