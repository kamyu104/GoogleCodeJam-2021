# Usage: pypy cheating_detection.test.py >data.in 2>data.out

from random import uniform, randint, seed
from math import exp
from sys import stderr

def f(x):
    return 1.0/(1.0+exp(-x))

seed(0)

T = 50
P = 86
S = 100
Q = 10000

print T
print Q

for case in xrange(T):
    s = [uniform(-3.0, 3.0) for _ in xrange(S)]
    q = [uniform(-3.0, 3.0) for _ in xrange(Q)]
    cheater = randint(0, S-1)
    print >>stderr, 'Case #%d: %s' % (case+1, cheater+1)
    for i in xrange(S):
        result = ['0']*Q
        for j in xrange(Q):
            if i == cheater and uniform(0.0, 1.0) <= 0.5:
                result[j] = '1'
            elif uniform(0.0, 1.0) <= f(s[i]-q[j]):
                result[j] = '1'
        print "".join(result)
