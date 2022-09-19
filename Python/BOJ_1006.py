import sys;input = sys.stdin.readline
def solve(k):
    for i in range(k, n):
        a[i + 1] = min(b[i] + 1, c[i] + 1)
        if i > 0 and li_1[i - 1] + li_1[i] <= w and li_2[i - 1] + li_2[i] <= w:
            a[i + 1] = min(a[i + 1], a[i - 1] + 2)
        if li_1[i] + li_2[i] <= w:
            a[i + 1] = min(a[i + 1], a[i] + 1)

        b[i + 1] = a[i + 1] + 1
        if i < n - 1 and li_1[i] + li_1[i + 1] <= w:
            b[i + 1] = min(b[i + 1], c[i] + 1)

        c[i + 1] = a[i + 1] + 1
        if i < n - 1 and li_2[i] + li_2[i + 1] <= w:
            c[i + 1] = min(c[i + 1], b[i] + 1)


for _ in range(int(input())):
    n, w = map(int, input().split())
    li_1 = list(map(int, input().split()))
    li_2 = list(map(int, input().split()))
    a, b, c = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    a[0], b[0], c[0] = 0, 1, 1
    solve(0)
    res = a[n]

    if n > 1:
        if li_1[0] + li_1[n - 1] <= w and li_2[0] + li_2[n - 1] <= w:
            a[1], b[1], c[1] = 0, 1, 1
            solve(1)
            res = min(res, a[n - 1] + 2)

        if li_1[0] + li_1[n - 1] <= w:
            a[1], b[1], c[1] = 1, 2, 2
            if li_2[0] + li_2[1] <= w:
                c[1] = 1
            solve(1)
            res = min(res, c[n - 1] + 1)

        if li_2[0] + li_2[n - 1] <= w:
            a[1], b[1], c[1] = 1, 2, 2
            if li_1[0] + li_1[1] <= w:
                b[1] = 1
            solve(1)
            res = min(res, b[n - 1] + 1)

    print(res)
