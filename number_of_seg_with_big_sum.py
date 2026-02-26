n, s = map(int, input().split())
arr = list(map(int, input().split()))

k = 0
j = 0
summ = 0
for i in range(n):
   
    while summ < s and j < n:
      summ += arr[j]
      j += 1
    if summ >= s : k += n - j + 1
    summ -= arr[i]

print(k)
      
