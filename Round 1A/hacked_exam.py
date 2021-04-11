# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Round 1A - Problem C. Hacked Exam
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/0000000000754750
#
# Time:  precompute: O(MAX_Q^2)
#        runtime:    O(Q)
# Space: O(MAX_Q^2), for nCr cache
#

from itertools import izip
from fractions import gcd

def hacked_exam():
    N, Q = map(int, raw_input().strip().split())
    A, S = [], []
    for _ in xrange(N):
        a, s = raw_input().strip().split()
        A.append(a)
        S.append(int(s))
    while N < 3:  # duplicate until N = 3
        A.append(A[-1])
        S.append(S[-1])
        N += 1
    for _ in xrange(len(nCr), Q+1):  # cached nCr, O(MAX_Q^2) time in total
        nCr.append([1] + [nCr[-1][i] + nCr[-1][i+1] for i in xrange(len(nCr[-1])-1)] + [1])

    an = sum(a == b == c for a, b, c in izip(*A))
    bn = sum(b == c != a for a, b, c in izip(*A))
    cn = sum(c == a != b for a, b, c in izip(*A))
    dn = sum(a == b != c for a, b, c in izip(*A))
    total = acount = bcount = ccount = dcount = 0
    for ar in xrange(an+1):
        # (1) ar + (bn-br) +    cr   +    dr   = S[0]    
        # (2) ar +    br   + (cn-cr) +    dr   = S[1]  
        # (3) ar +    br   +    cr   + (dn-dr) = S[2]
        br = (S[1]+S[2]-cn-dn)//2-ar  # [(2)+(3)]/2, since at least one br exists and (S[1]+S[2]-cn-dn)//2 is constant, so (S[1]+S[2]-cn-dn)%2 is always 0
        cr = (S[2]+S[0]-bn-dn)//2-ar  # [(3)+(1)]/2, since at least one cr exists and (S[2]+S[0]-bn-dn)//2 is constant, so (S[2]+S[0]-bn-dn)%2 is always 0
        dr = (S[0]+S[1]-bn-cn)//2-ar  # [(1)+(2)]/2, since at least one dr exists and (S[0]+S[1]-bn-cn)//2 is constant, so (S[0]+S[1]-bn-cn)%2 is always 0
        if not (0 <= br <= bn and 0 <= cr <= cn and 0 <= dr <= dn):  # ar is invalid
            continue
        ways = nCr[an][ar] * nCr[bn][br] * nCr[cn][cr] * nCr[dn][dr]
        total += ways
        acount += ways*ar
        bcount += ways*br
        ccount += ways*cr
        dcount += ways*dr
    result = []
    for a, b, c in izip(*A):
        if a == b == c:
            result.append(a if acount >= total*an-acount else "TF"[a == 'T'])
        elif b == c != a:
            result.append(b if bcount >= total*bn-bcount else a)
        elif c == a != b:
            result.append(c if ccount >= total*cn-ccount else b)
        elif a == b != c:
            result.append(a if dcount >= total*dn-dcount else c)
    count = max(acount, total*an-acount) + max(bcount, total*bn-bcount) + max(ccount, total*cn-ccount) + max(dcount, total*dn-dcount)
    g = gcd(count, total)
    return "%s %s/%s" % ("".join(result), count//g, total//g)

nCr = [[1]]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, hacked_exam())
