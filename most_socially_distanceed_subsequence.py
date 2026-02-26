t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    p = 1
    sub_sec = [arr[0]]
    pdif = 0

    while p < n:
        dif = arr[p - 1] - arr[p]
        
        if pdif > 0 and dif < 0:
            sub_sec.append(arr[p-1])
        elif pdif < 0 and dif > 0:
            sub_sec.append(arr[p-1])
        if p == n-1:
            sub_sec.append(arr[p])
        p += 1
        pdif = dif
    
    print(len(sub_sec))
    print(*sub_sec)

    
    
        

