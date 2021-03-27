# Time:  O(N)
# Space: O(1)

def reversort_engineering():
    N, C = map(int, raw_input().strip().split())

    if not (N-1 <= C <= (N+2)*(N-1)//2):
        return "IMPOSSIBLE"
    result = [0]*N
    for i in xrange(N):
        l = min(C-(N-1-i)+1, N-i)  # greedy
        C -= l
        if l != N-i:
            remain = range(i+1, N+1)
            remain[:l] = remain[:l][::-1]
            if i%2 == 0:
                result[N-1-i//2+1-len(remain):N-1-i//2+1] = remain
            else:
                result[i//2:i//2+len(remain)] = remain[::-1]
            break
        if i%2 == 0:
            result[N-1-i//2] = i+1
        else:
            result[i//2] = i+1
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, reversort_engineering())
