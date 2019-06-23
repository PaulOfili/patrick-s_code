# 1
# take the input
input_arr = [[1, 3, 602],
             [1, 2, 256],
             [2, 3, 411]]
# n, e = map(int, input().strip().split())
n, e = [3, 3]

adj = [[] for i in range(n)]
for i in range(e):
    # x, y, r = map(int, input().strip().split())
    x, y, r = input_arr[i]
    x -= 1
    y -= 1
    adj[x].append((y, +r % 10))
    adj[y].append((x, -r % 10))

print(adj)
# initialize arrays
visn = [False]*n
vis = [[False]*10 for x in range(n)]
C = [[0]*10 for x in range(n)]
D = [None]*n

# perform BFS/DFS
for x in range(n):
    if visn[x]: continue

    # compute C[x][d] for all d using BFS/DFS
    stack = [(x, 0)]
    current = []
    vis[x][0] = True
    while stack:
        xi, di = stack.pop()
        if not visn[xi]:
            visn[xi] = True
            current.append(xi)
        C[x][di] += 1
        D[xi] = di
        for xj, dj in adj[xi]:
            dij = (di + dj) % 10
            if not vis[xj][dij]:
                vis[xj][dij] = True
                stack.append((xj, dij))

    # compute C[xi] for all other xi
    for xi in current:
        for di in range(10):
            C[xi][di] = C[x][(di + D[xi]) % 10]


# print the answers
for di in range(10):
    ans = 0
    for xi in range(n):
        # adjustment
        ans += C[xi][di] - vis[xi][(di + D[xi]) % 10]
    print(ans)



# # 2
# n, e = map(int, raw_input().strip().split())
#
# adj = [[] for i in xrange(n)]
# for ee in xrange(e):
#     a, b, c = map(int, raw_input().strip().split())
#     a -= 1
#     b -= 1
#     adj[a].append((b, +c%10))
#     adj[b].append((a, -c%10))
#
# ovis = [False]*n
# vis = [[False]*10 for i in xrange(n)]
#
# ans = [0]*10
# for s in xrange(n):
#     if ovis[s]: continue
#     queue = [(s,0)]
#     vis[s][0] = True
#     f = 0
#     ct = [0]*10
#     while f < len(queue):
#         i,d = queue[f]; f += 1
#         ct[d] += 1
#         for j,nd in adj[i]:
#             nd = (nd+d)%10
#             if not vis[j][nd]:
#                 vis[j][nd] = True
#                 queue.append((j,nd))
#
#     for i,d in queue:
#         if ovis[i]: continue
#         ovis[i] = True
#         d = -d%10
#         for nd in xrange(10):
#             ans[(nd+d)%10] += ct[nd] - vis[i][nd]
#
# for v in ans: print v

# SAMPLE INPUT
# 3 3
# 1 3 602
# 1 2 256
# 2 3 411

# ANSWER
# 0
# 2
# 1
# 1
# 2
# 0
# 2
# 1
# 1
# 2