n = int(input())
tree = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    tree[int(input())].append(i)

check = True

list = [1]
while list:
    node = list.pop(0)
    count = 0
    for child in tree[node]:
        if not tree[child]:
            count += 1
        else:
            list.append(child)

    if count < 3:
        check = False
        break

if check:
    print("Yes")
else:
    print("No")