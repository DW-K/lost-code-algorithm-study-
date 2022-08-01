def low_channel(lst,N):
    for i in range(N,-1,-1):
        for j in range(len(str(i))):
            if str(i)[j] in lst:
                break
            elif j==len(str(i))-1:
                return (N-i)+len(str(i))
    return 1000001

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