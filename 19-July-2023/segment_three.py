from itertools import product
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 10**9
    for x, y in product([0, 1, 2], repeat=2):
        moves = x + y
        p1, p2 = a[0] + x, a[1] + y
        for i in range(2, n):
            cur = p1 + p2 + a[i]
            increment = (-cur)%3
            moves += increment
            p1, p2 = p2, a[i]+increment
        ans = min(ans, moves)
    print(ans)