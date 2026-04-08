def find_subs(arr, x):
    l , r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    cur_max = 10**18
    check = True

    for i in range(n - 1, -1, -1):
        keep = a[i] if a[i] <= cur_max else -10**18

        k = find_subs(b, cur_max + a[i])
        if k != -1:
            change = b[k] - a[i]
        else:
            change = -10**18

        best = max(keep, change)

        if best == -10**18:
            check = False
            break

        cur_max = best

    print("YES" if check else "NO")