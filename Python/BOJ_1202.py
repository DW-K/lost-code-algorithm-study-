import sys;input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
jewel, bag = [], []
for _ in range(n):
    tmp = tuple(map(int, input().split()))
    heapq.heappush(jewel, tmp)
bag = sorted([int(input()) for _ in range(k)])
res, tmp = 0, []
for i in range(k):
    while jewel and bag[i] >= jewel[0][0]:
        m, v = heapq.heappop(jewel)
        heapq.heappush(tmp, (-v, -m))
    if tmp: res += -heapq.heappop(tmp)[0]
print(res)