import sys

input = sys.stdin.readline

def count_people(people):
    ret = 0
    while people > 0:
        ret += people & 1
        people >>= 1
    return ret


def possible(seat, prev_people, curr_people):
    if (seat & curr_people) > 0:
        return False
    if ((prev_people << 1) & curr_people) > 0:
        return False
    if ((prev_people >> 1) & curr_people) > 0:
        return False
    if ((curr_people << 1) & curr_people) > 0:
        return False
    return True

def solve(row, prev_people, seats):
    if row == n:
        return 0
    if memo[row][prev_people] != -1:
        return memo[row][prev_people]
    ret = 0
    for curr_people in range(2 ** m):
        if possible(seats[row], prev_people, curr_people):
            ret = max(
                ret, solve(row + 1, curr_people, seats) + count_people(curr_people)
            )
    memo[row][prev_people] = ret
    return memo[row][prev_people]

for _ in range(int(input())):
    n, m = map(int, input().split())
    li = [list(input()) for _ in range(n)]
    memo = [[-1] * (2**m) for _ in range(n)]
    seats = []
    for i in range(n):
        seat = 0
        for j in range(m):
            seat <<= 1
            if li[i][j] == 'x':
                seat += 1
        seats.append(seat)
    print(solve(0, 0, seats))