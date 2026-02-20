t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    swaps = []

    for i in range(n):
        for j in range(n - i -1):
            if a[j] > a[j+1]:
                count += 1
                swaps.append([1, j + 1])
                a[j] , a[j+1] = a[j+1], a[j]
            if b[j] > b[j+1]:
                count += 1
                swaps.append([2, j + 1])
                b[j] , b[j+1] = b[j+1], b[j]

   

    for i in range(n):

        if a[i] > b[i]:
            count += 1
            swaps.append([3, i + 1])
            a[i] , b[i] = b[i], a[i] 

    print(count)
   
    for i in swaps:
        print(*i)

   
    
    


    
