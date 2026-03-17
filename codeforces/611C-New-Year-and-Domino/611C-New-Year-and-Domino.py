def build_prefix(a, r, c):
    p = [[0]*(c+1) for _ in range(r+1)]
    for i in range(1, r+1):
        for j in range(1, c+1):
            p[i][j] = (
                a[i-1][j-1]
                + p[i-1][j]
                + p[i][j-1]
                - p[i-1][j-1]
            )
    return p


PH = build_prefix(H, h, w-1)
PV = build_prefix(V, h-1, w)


def query(p, r1, c1, r2, c2):
    if r1 > r2 or c1 > c2:
        return 0
    return (
        p[r2][c2]
        - p[r1-1][c2]
        - p[r2][c1-1]
        + p[r1-1][c1-1]
    )


q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    horizontal = query(PH, r1, c1, r2, c2-1)
    vertical = query(PV, r1, c1, r2-1, c2)

    print(horizontal + vertical)