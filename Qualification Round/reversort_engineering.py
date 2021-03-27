# Time:  O(N^2)
# Space: O(N)

def reverse(L, i, j):
    while i < j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1

def reversort_engineering():
    N, C = map(int, raw_input().strip().split())

    if not (N-1 <= C <= (N+2)*(N-1)//2):
        return "IMPOSSIBLE"
    operations = []
    for i in xrange(N-1):
        m = i+min(C-(N-1-i)+1, N-i)-1  # greedy
        C -= m-i+1
        operations.append((i, m))
    result = range(1, N+1)
    for i, j in reversed(operations):
        reverse(result, i, j)
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reversort_engineering())
