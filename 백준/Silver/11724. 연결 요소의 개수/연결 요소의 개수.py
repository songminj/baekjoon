import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    visited[i] = True
    for w in adj_dic[i]:
        if not visited[w]:
            dfs(w)

# n :  정점, m : 간선의 개수
n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
adj_dic = { i : [] for i in range(1, n+1)}

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    adj_dic[start] += [end]
    adj_dic[end] += [start]
# print(adj_dic)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)