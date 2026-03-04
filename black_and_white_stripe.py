from collections import Counter
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    count = Counter()
    min_change = float('inf')
    r, l, res = 0 , 0, 0

    while r < n:
        if s[r] == "W":
            res += 1
        count["B"] += 1

        if count["B"] == k:
            min_change = min(min_change, res)

        while count["B"] >= k:
            if s[l] == "W":
                res -= 1
            l += 1
            count["B"] -= 1
        r += 1

    print(min_change)

        
            
        

