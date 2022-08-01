import sys

sys.stdin = open('input.txt','r')

input = sys.stdin.readline

N = int(input())
M = int(input())
ls = (list(map(str,input().split())))
target = []
cnt = 0
jaritsu = len(str(N))
temp = 100
min = abs(temp-N)# 최소차이
near = 100 #가장 가까운 수

for i in range(1000000):
    if any(ls in str(i) for ls in ls) == False:
        target.append(i)
for j in target:
    sub = abs(N-j)
    if sub < min:
        min = sub
        near = j

if abs(N-100)>(len(str(near)) + min):
    print((len(str(near)) + min))
else:
    print(abs(N-100))

# print(min)
# print(near)


#제일 가까운 숫자를 만든다
#자릿수만큼의 범위 내에서 예를 들어 n이 100 이면 0~999
#고장난 버튼을 포함하지 않고 가장 가까운 수를 찾는다
#직접 빼는거보다 버튼누르는게 횟수 작으면 그렇게 하고
#아니면 직접빼 
#거기서 뺀다