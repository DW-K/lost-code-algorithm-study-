import sys
sys.stdin = open('input.txt')
import math

# 이분탐색
def lowerbound(li, n):
    start, end = 0, len(li)
    while start < end:
        mid = (start + end) // 2
        if n <= li[mid]:
            end = mid
        else:
            start = mid + 1
    return start


def solve(s, e, candy):
    # 가져갈 사탕이 없으면 종료
    if candy == 0:
        return 0
    l, r = min(s, e), max(s, e)
    # 메모이제이션
    if dp[s][e] != -1:
        return dp[s][e]
    dp[s][e] = math.inf
    # 우측의 사탕을 가져가는 경우 없어지는 사탕의 수
    # 1*3 5*2 9*1
    if r < n:
        dp[s][e] = min(dp[s][e], solve(l, r + 1, candy - 1) + candy * (li[r + 1] - li[e]))
    # 좌측의 사탕을 가져가는 경우 없어지는 사탕의 수
    if l > 0:
        dp[s][e] = min(dp[s][e], solve(r, l - 1, candy - 1) + candy * (li[e] - li[l - 1]))
    return dp[s][e]


n, m = map(int, input().split())
# 0을 포함해서 정렬
li = [0] * (n+1)
for i in range(n):
    li[i] = int(input())
li.sort()
# 0이 있는 인덱스 뽑기
s = lowerbound(li, 0)
res = 0
# 사탕을 1개 ~ n개 가져가는 경우의 수 나누기
for i in range(1, n+1):
    dp = [[-1] * (n+1) for _ in range(n+1)]
    # 처음은 0에서 시작, 총 가져갈 사탕의수 i*m에서 없어지는 사탕의 수 빼기
    res = max(res, i * m - solve(s, s, i))

print(res)

# 없어지는 사탕의 수 = 누적이동 거리의 합
# 누적 이동거리 = 첫 이동 거리 * i + 두번째 이동거리 * (i - 1) + ... 마지막 이동거리 * 1
# -3 0 1 6