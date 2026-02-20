n, k  = map(int, input().split())
arr = list(map(int, input().split()))
diff = []
for i in range(1, n):
    diff.append(arr[i] - arr[i-1])
diff.sort()
summ = sum(diff[:n-k])
print(summ)
