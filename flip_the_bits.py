t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())

    balance = [0]*n
    ones = 0

    for i in range(n):
        if a[i] == '1':
            ones += 1
        zeros = i + 1 - ones
        if ones == zeros:
            balance[i] = 1

    # print(balance)

    flipped = 0
    possible = True

    for i in range(n-1, -1, -1):
        cur = a[i]

        if flipped:
            cur = '1' if cur == '0' else '0'

        if cur == b[i]:
            continue

        if balance[i] == 0:
            possible = False
            break

        flipped ^= 1

    if possible:
        print("YES")
    else:
        print("NO")


    
