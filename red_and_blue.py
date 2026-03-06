def prefix (arr):
    max_prefix = 0
    summ = 0
    for i in arr:
        summ += i
        max_prefix = max(summ, max_prefix)
    return max_prefix



t = int(input())
for _ in range(t):
    n = int(input())
    reds = list(map(int, input().split()))
    m = int(input())
    blues = list(map(int, input().split()))
    print(prefix(reds) + prefix(blues))


    
    

