import sys;input = sys.stdin.readline
def dfs(s):
    if visited[s]: return 0
    visited[s] = True
    for i in li[s]:
        if res[i] == 0 or dfs(res[i]):
            res[i] = s
            return 1
    return 0

n, m = map(int, input().split())
li = [0] + [list(map(int, input().split()))[1:] for _ in range(n)]
res, ans = [0] * (m + 1), 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if dfs(i): ans += 1
print(ans)