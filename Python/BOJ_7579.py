from sys import stdin
# 앱의 갯수/ 확보해야할 바이트 입력 받기
n, m = map(int, stdin.readline().split())
# 메모리와 비용을 각각 리스트로 받기
bytes = list(map(int, stdin.readline().split()))
fees = list(map(int, stdin.readline().split()))
bytes.insert(0,0)
fees.insert(0,0)
# dp table을 빈 2차원 배열로 선언
cost = [[0 for _ in range(sum(fees)+1)] for _ in range(n+1)]
# 나올 수 있는 비용의 최댓값으로 초기화
result = 10001
# dynamic programming
for i in range(1,n+1):
    for j in range(sum(fees)+1):
        if fees[i] > j:
            cost[i][j] = cost[i-1][j]
        else: # fees[i] <= j
            cost[i][j] = max(cost[i-1][j],cost[i-1][j-fees[i]]+bytes[i])
        # 최소 메모리를 넘었을 때 최소 비용으로 할당
        if cost[i][j] >= m:
            result = min(result,j)
            
print(result)