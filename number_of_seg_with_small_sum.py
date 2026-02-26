n, s = map(int, input().split())
arr = list(map(int, input().split()))

k = 0
j = 0
summ = 0
for i in range(n):
    summ += arr[i]
    
    while summ > s :
        summ -= arr[j]
        j += 1

    k += i - j + 1

print(k)
    
