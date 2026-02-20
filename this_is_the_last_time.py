t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(n))
   

    arr.sort(key=lambda x: x[0])
    for i in range(n):
        if  k >= arr[i][0] and k <= arr[i][1]:
            k = max(k, arr[i][2])
            
        
    print(k)
