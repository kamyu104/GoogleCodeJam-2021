# Copyright (c) 2021 kamyu. All rights reserved.
#
# Google Code Jam 2021 Virtual World Finals - Problem E. Infinitree
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000436329/000000000084fc01
#
# Time:  O(N^3.5 * logN + N^3 * logB), pass in PyPy3 but Python3
# Space: O(N^2.5 * logN + N^2 * logB)
#
# concise solution of infinitree.py
#

# Template modified from:
# https://github.com/kamyu104/GoogleCodeJam-2017/blob/master/Round%202/beaming_with_joy.py
def strongly_connected_components(graph):  # Time: O(|V| + |E|) = O(N + 2N) = O(N), Space: O(|V|) = O(N)
    def strongconnect(v, index_counter, index, lowlinks, stack, stack_set, result):
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        stack_set.add(v)
        stack.append(v)
        for w in (graph[v] if v in graph else []):
            if w not in index:
                strongconnect(w, index_counter, index, lowlinks, stack, stack_set, result)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in stack_set:
                lowlinks[v] = min(lowlinks[v], index[w])
        if lowlinks[v] == index[v]:
            connected_component = []
            w = None
            while w != v:
                w = stack.pop()
                stack_set.remove(w)
                connected_component.append(w)
            result.append(set(connected_component))

    index_counter, index, lowlinks = [0], {}, {}
    stack, stack_set = [], set()
    result = []
    strongconnect(ROOT_COLOR, index_counter, index, lowlinks, stack, stack_set, result)  # modified, only care about reachable colors
    return result

# return cycle_adj, cycle_length only if all reachable colors belong to at most one cycle
def find_cycles(graph):  # Time: O(N), Space: O(N)
    cycle_adj, cycle_length = {}, {}
    for scc in strongly_connected_components(graph):
        if any(sum(int(x in scc) for x in graph[node]) == 2 for node in scc):  # this is optional optimization
            return {}, {}  # have a reachable color belonging to more than one cycle, we only need to run single step solution
        if any(sum(int(x in scc) for x in graph[node]) != 1 for node in scc):
            continue
        node = next(iter(scc))
        for _ in range(len(scc)):
            cycle_adj[node] = [side for side, x in enumerate(graph[node]) if x in scc][0]
            cycle_length[node] = len(scc)
            node = graph[node][cycle_adj[node]]
    return cycle_adj, cycle_length

def floor_log2_x(x):  # Time: O(logx)
    return x.bit_length()-1

def identity_matrix(N):  # Time: O(N)
    return [[int(i == j) for j in range(N)] for i in range(N)]

def e(i, N):  # Time: O(N)
    return [int(j == i) for j in range(N)]

def matrix_mult(A, B, INF): # Time: O(N^2) if A is a 1 x N matrix and B is a N x N matrix, O(N^3) if A, B are both N x N matrixs
    result = [[0]*len(B[0]) for _ in range(len(A))]
    B_T = list(zip(*B))
    for result_i, A_i in zip(result, A):
        for j, B_T_i in enumerate(B_T):
            for A_i_j, B_T_i_j in zip(A_i, B_T_i):
                result_i[j] += A_i_j*B_T_i_j
                if result_i[j] > INF:
                    result_i[j] = INF
                    break
    return result

def matrix_add(A, B, INF):  # Time: O(N) if A, B are both 1 x N matrixs, O(N^2) if A, B are both N x N matrixs
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for result_i, A_i, B_i in list(zip(result, A, B)):
        for j in range(len(result_i)):
            result_i[j] = A_i[j]+B_i[j]
            if result_i[j] > INF:
                result_i[j] = INF
    return result

# build [M, M^2, ..., M^(2^logx)] and [I, (I + M), (I + M + M^2 + M^3), (I + M + ... + M^(2^logx-1))]
def build_powers_and_power_series(N, M, INF, x):  # Time: O(N^3 * logx)
    logx = floor_log2_x(x)
    I = identity_matrix(N)
    # M_powers[i] for i in range(1+logx):
    # 0: M
    # 1: M^2
    # ...
    # logx: M^(2^logx)
    M_powers = [M]
    for _ in range(logx):  # Time: O(N^3 * logx)
        M_powers.append(matrix_mult(M_powers[-1], M_powers[-1], INF))
    # M_power_series[i] for i in range(1+logx):
    # 0: I
    # 1: (I + M) * I = I + M
    # 2: (I + M^2) * (I + M) = I + M + M^2 + M^3
    # ...
    # logx: (I + M^(2^(logx-1))) * (I + M + ... + M^(2^(logx-1)-1)) = I + M + ... + M^(2^logx-1)
    M_power_series = [I]
    for i in range(logx):  # Time: O(N^3 * logx)
        matrix = matrix_add(I, M_powers[i], INF)
        M_power_series.append(matrix_mult(matrix, M_power_series[-1], INF))
    return M_powers, M_power_series

# V * M^x by vector-matrix or matrix-matrix exponentiation
def get_V_M_power_x(M_powers, INF, V, x):  # Time: O(N^2 * logx) if V is a 1 x N matrix, O(N^3 * logx) if V is a N x N matrix
    basis, i = 1, 0
    while basis <= x:
        if x&basis:
            V = matrix_mult(V, M_powers[i], INF)
        basis, i = basis<<1, i+1
    return V

# v * (I + M + M^2 + ... + M^x) by vector-matrix exponentiation
def get_v_M_power_series_x(N, M_powers, M_power_series, INF, v, x):  # Time: O(N^2 * logx)
    x += 1
    u = [0]*N
    basis, i = 1, 0
    while basis <= x:
        if x&basis:
            # new_Pr = P_r*M^(2^i) + P_(2^i)
            # new_u = v * new_Pr = v * (P_r*M^(2^i) + P_(2^i)) = u*M^(2^i) + v*P_(2^i)
            u = matrix_add(matrix_mult([u], M_powers[i], INF),
                           matrix_mult([v], M_power_series[i], INF),
                           INF)[0]
        basis, i = basis<<1, i+1
    return u

def get_depth(N, M_powers, M_power_series, INF, v, x):  # Time: O(N^2 * logx)
    logx = floor_log2_x(x)
    result = 0
    u = [0]*N
    basis = 1<<logx
    # find max r s.t. sum(v * P_r) < x, where P_r = I + M + M^2 + ... + M^(r-1)
    for i in reversed(range(logx+1)):  # O(N^2 * logx)
        # new_Pr = P_r*M^(2^i) + P_(2^i)
        # new_u = v * new_Pr = v * (P_r*M^(2^i) + P_(2^i)) = u*M^(2^i) + v*P_(2^i)
        new_u = matrix_add(matrix_mult([u], M_powers[i], INF),
                           matrix_mult([v], M_power_series[i], INF),
                           INF)[0]
        if sum(new_u) < x:
            u = new_u
            result |= basis
        basis >>= 1
    return result

def get_single_step_position(M_powers, INF, ec, h, x):  # Time: O(N^2 * logx)
    left_cnt = sum(get_V_M_power_x(M_powers, INF, [ec], h-1)[0])
    return (LEFT, x) if x < left_cnt else (RIGHT, x-left_cnt)

def get_multiple_steps_position(M_powers, Mh_power_series, INF, logp, v, delta_h, ec, x):  # Time: O(N^2 * log(delta_h))
    left_cnt = sum(get_V_M_power_x(M_powers, INF, matrix_mult([v], Mh_power_series[logp], INF), delta_h)[0])
    mid_cnt = sum(get_V_M_power_x(M_powers, INF, [ec], delta_h)[0])
    return 0 <= x-left_cnt < mid_cnt, x-left_cnt

def infinitree():
    N, A, B = list(map(int, input().strip().split()))
    L = list(map(int, input().strip().split()))
    R = list(map(int, input().strip().split()))

    N += 1
    if A > B:
        A, B, = B, A
    INF = B
    M = [[0]*N for _ in range(N)]
    graph = {LEAF_COLOR:[]}
    for i in range(ROOT_COLOR, N):
        M[i][L[i-1]] += 1
        M[i][R[i-1]] += 1
        graph[i] = [L[i-1], R[i-1]]

    Mh_powers, Mh_power_series = {}, {}
    Mh_powers[1], Mh_power_series[1] = build_powers_and_power_series(N, M, INF, B)  # Time: O(N^3 * logB)
    h1 = get_depth(N, Mh_powers[1], Mh_power_series[1], INF, e(ROOT_COLOR, N), A)
    h2 = get_depth(N, Mh_powers[1], Mh_power_series[1], INF, e(ROOT_COLOR, N), B)
    x1 = A-sum(get_v_M_power_series_x(N, Mh_powers[1], Mh_power_series[1], INF, e(ROOT_COLOR, N), h1-1))-1
    x2 = B-sum(get_v_M_power_series_x(N, Mh_powers[1], Mh_power_series[1], INF, e(ROOT_COLOR, N), h2-1))-1
    cycle_adj, cycle_length = find_cycles(graph)
    c  = ROOT_COLOR
    while (h1, x1) != (0, 0):
        if c not in cycle_adj:  # enter none-only-1-cycle node, Time: O(N^2 * logB) => Total Time: O(N^2 * (logB)^2)
            side1, new_x1 = get_single_step_position(Mh_powers[1], INF, e(L[c-1], N), h1, x1)
            side2, new_x2 = get_single_step_position(Mh_powers[1], INF, e(L[c-1], N), h2, x2)
            if side1 != side2:  # found lca
                break
            h1, x1 = h1-1, new_x1
            h2, x2 = h2-1, new_x2
            c = (L[c-1] if side1 == LEFT else R[c-1])
            continue
        # path from root to lca enter a new unseen cycle, we can speed up in this part of path,
        # we run this multiple steps solution only if all reachable colors belong to at most one cycle,
        # otherwise, the binary tree grows exponentially with height at most O(logB) so that single step solution is fast enough,
        # and also saves the extra time and space cost from multiple steps solution
        h = cycle_length[c]
        if h not in Mh_powers:  # lazy init, sum(distinct h) = N => distinct h at most O(sqrt(N)) times, each Time: O(N^3 * logh + N^3 * log(hi)) => Total Time: O(N^3.5 * logN + (N^3.5 * log(logB) + N^3 * logB)) = O(N^3.5 * logN + N^3 * logB) assumed O(N) = O(logB)
            Mh_powers[h], Mh_power_series[h] = build_powers_and_power_series(N, get_V_M_power_x(Mh_powers[1], INF, identity_matrix(N), h), INF, min(h1, h2))
        cycle, v = [], [0]*N
        for x in reversed(range(h)):  # Time: O(h * N^2 * logN) => Total Time O(N^3 * logN)
            if cycle_adj[c] == RIGHT:
                v = matrix_add([v], [get_V_M_power_x(Mh_powers[1], INF, [e(L[c-1], N)], x)[0]], INF)[0]
                c = R[c-1]
            else:
                c = L[c-1]
            cycle.append(c)
        p, logp = 1, 0
        while (p*2)*h < min(h1, h2):
            p, logp = p*2, logp+1
        while p > 1:  # logp times => Total Time: O(k cycles * logp times * (N^2 * log(delta_h))) = O(N^3 * log(logB)^2 + N^2 * (logB)^2) = O(N^3 * logB) assumed O(N) = O(logB)
            if min(h1, h2) - p*h <= 0:
                p, logp = p//2, logp-1
                continue
            ok1, new_x1 = get_multiple_steps_position(Mh_powers[1], Mh_power_series[h], INF, logp, v, h1-p*h, e(c, N), x1)
            ok2, new_x2 = get_multiple_steps_position(Mh_powers[1], Mh_power_series[h], INF, logp, v, h2-p*h, e(c, N), x2)
            if not ok1 or not ok2:
                p, logp = p//2, logp-1
                continue
            h1, x1 = h1-p*h, new_x1
            h2, x2 = h2-p*h, new_x2
            p, logp = p//2, logp-1
        for x in cycle:  # no need to do multiple steps solution
            del cycle_adj[x]
    return h1+h2

LEFT, RIGHT = range(2)
LEAF_COLOR, ROOT_COLOR = range(2)  # leaf color is 0, root color is 1
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, infinitree()))
