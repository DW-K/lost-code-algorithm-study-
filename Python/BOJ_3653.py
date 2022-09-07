from math import ceil, log
import sys;input = sys.stdin.readline

# 세그먼트 트리 생성
def init(arr, tree, i, left, right):
    if left == right:
        tree[i] = arr[left]
        return tree[i]
    mid = left + (right - left) // 2
    tree[i] = init(arr, tree, i * 2, left, mid) + init(arr, tree, i * 2 + 1, mid + 1, right)
    return tree[i]

# 구간합 꺼내기
def search(tree, i, start, end, left, right):
    # 요청 값이 노드를 벗어난다면 연산할 필요x
    if end < left or right < start:
        return 0
    # 요청 값이 노드안에 완전히 포함된다면 반환
    if left <= start and end <= right:
        return tree[i]
    # 아닌 경우 계속 탐색 (요청값이 노드보다 클 경우, 요청값과 노드가 걸칠 경우)
    mid = start + (end - start) // 2
    return search(tree, i * 2, start, mid, left, right) + search(tree, i * 2 + 1, mid + 1, end, left, right)

# idx의 값을 diff만큼 바꾸고 싶을 때
def update(tree, i, start, end, idx, diff):
    # 바꿔야 하는 값이 노드안에 없다면 연산x
    if start > idx or idx > end:
        return
    # 노드 안에 있으면 무조건 diff만큼 바꾸기
    tree[i] += diff
    # idx가 포함된 구간 합들의 노드 값을 전부다 바꿀 때 까지 재연산
    if start != end:
        mid = start + (end - start) // 2
        update(tree, i * 2, start, mid, idx, diff)
        update(tree, i * 2 + 1, mid + 1, end, idx, diff)


def solve():
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    # 앞으로 꺼낼 수행 횟수만큼 0으로, 가지고 있는 영화의 갯수 만큼 1로 초기화 되어있는 배열 생성 (초기의 영화 상태)
    mov = [0] * (m) + [1] * n
    # 꺼내서 올린 인덱스 기록할 배열 생성
    loc = [0] * (n + 1)
    # segment tree init
    segment_tree = [0] * pow(2, ceil(log(len(mov), 2) + 1))
    init(mov, segment_tree, 1, 0, len(mov) - 1)
    for i in range(m):
        cnt = 0
        # 꺼내야 하는 영화
        tmp = li[i] - 1
        # 한번도 보지 않은 영화일 경우
        if mov[tmp + m]:
            # 원래의 위치를 기준으로 구간합
            cnt += search(segment_tree, 1, 0, len(mov) - 1, 0, tmp + m - 1)
            # 꺼내서 위로 올려주기
            mov[tmp + m] = 0
            mov[m - i - 1] = 1
            # 트리의 값도 업데이트
            update(segment_tree, 1, 0, len(mov) - 1, tmp + m, -1)
            update(segment_tree, 1, 0, len(mov) - 1, m - i - 1, 1)
            # 꺼내서 올린 위치 기록
            loc[tmp] = m - i - 1
        # 이미 한번 이상 봐서 위치가 달라진 경우
        else:
            # 저장해 둔 위치를 기준으로 구간합
            cnt += search(segment_tree, 1, 0, len(mov) - 1, 0, loc[tmp] - 1)
            # 저장해 두었던 위치 갱신
            mov[loc[tmp]] = 0
            mov[m - i - 1] = 1
            # 트리 업데이트
            update(segment_tree, 1, 0, len(mov) - 1, loc[tmp], -1)
            update(segment_tree, 1, 0, len(mov) - 1, m - i - 1, 1)
            # 꺼내서 올린 위치 기록
            loc[tmp] = m - i - 1
        print(cnt, end=' ')
    print()


for _ in range(int(input())):
    solve()