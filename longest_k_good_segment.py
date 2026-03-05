from collections import Counter
n, k = map(int, input().split())
s = list(input().split())
l, r = 0, 0
long_seg = 0
x,y = 0,0
counter = Counter()
while r < n:
    counter[s[r]] += 1

    while len(counter) > k:
        counter[s[l]] -= 1
        if counter[s[l]] == 0:
            del counter[s[l]]
        l += 1
    w = r - l + 1
    if w > long_seg:
        long_seg = w
        x , y = l + 1, r + 1
    r += 1


print(x,y)


