import sys;input = sys.stdin.readline
# d의 방향에 따라 돌리는 숫자 반환
def mod(a, b, c):
    return (a + b) % 10 if c > 0 else (a - b + 10) % 10

def go(idx, x, y, z, d):
    # 마지막 번호면 종료
    if idx == n:
        return 0
    # 메모이제이션
    if dp[idx][x][y][z][d] != -1:
        return dp[idx][x][y][z][d]
    dp[idx][x][y][z][d] = 2100000000
    # x를 돌렸을 때 원하는 위치일 경우
    if (int(s[idx]) + x) % 10 == int(e[idx]):
        # 다음 칸으로 넘어가서 검사
        dp[idx][x][y][z][d] = min(go(idx + 1, y, z, 0, int(not d)), go(idx + 1, y, z, 0, d))
        return dp[idx][x][y][z][d]
    # 한칸 ~ 3칸 돌릴 때
    for k in range(1, 4):
        # x만 돌릴 때
        dp[idx][x][y][z][d] = min(
            dp[idx][x][y][z][d], go(idx, mod(x, k, d), y, z, d) + 1)
        # x, y 돌릴 때
        dp[idx][x][y][z][d] = min(
            dp[idx][x][y][z][d], go(idx, mod(x, k, d), mod(y, k, d), z, d) + 1)
        # x, y, z 돌릴 때
        dp[idx][x][y][z][d] = min(
            dp[idx][x][y][z][d], go(idx, mod(x, k, d), mod(y, k, d), mod(z, k, d), d) + 1)
    return dp[idx][x][y][z][d]

n = int(input())
s = input()
e = input()
dp = [[[[[-1] * 2 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(101)]
print(min(go(0, 0, 0, 0, 0), go(0, 0, 0, 0, 1)))