from collections import Counter

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))



if n < m:
    arr = arr1
    c_arr = Counter(arr2)
else:
    arr = arr2
    c_arr = Counter(arr1)



c = 0
for i in arr:
    c += c_arr[i]

print(c)
