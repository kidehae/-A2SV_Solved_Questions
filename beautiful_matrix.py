row = []
x = 0
y = 0
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        x = i
        y = row.index(1)
        break
moves = abs(2 - x) + abs(2 - y)
print(moves)

    
       
