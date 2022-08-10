from sys import stdin

n = int(stdin.readline())
# 5로 나누었을 때 나머지가 0이나 2일 경우 후공이 필승
if n%5==0 or n%5==2:
    print('CY')
else:
    print('SK')