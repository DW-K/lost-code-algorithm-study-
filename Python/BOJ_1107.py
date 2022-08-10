# 현재 채널보다 아래를 탐색
def low_channel(lst,N):
    for i in range(N,-1,-1):
        for j in range(len(str(i))):
            # 고장난 버튼이 있을 경우 i 값을 바꿔 다시 탐색
            if str(i)[j] in lst:
                break
            # 없이 끝났을 경우 값을 리턴
            elif j==len(str(i))-1:
                return (N-i)+len(str(i))
    return 1000001
# 현재 채널보다 위를 탐색
def high_channel(lst,N):
    for i in range(N,1000001):
        for j in range(len(str(i))):
            if str(i)[j] in lst:
                break
            elif j==len(str(i))-1:
                return (i-N)+len(str(i))
    return 1000001
    
N = int(input())
M = int(input())
if M:
    broken_lst = list(map(str,input().split()))
    best_channel = min(high_channel(broken_lst,N),low_channel(broken_lst,N),abs(100-N))
    print(best_channel)
else:
    print(min(len(str(N)),abs(100-N)))