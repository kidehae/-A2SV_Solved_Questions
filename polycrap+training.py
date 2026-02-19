n = int(input())
arr = list(map(int, input().split()))

k = 1
arr.sort()
count = 0
for i in range(n):
    if arr[i] >= k:
        count += 1
        k += 1

print(count)
