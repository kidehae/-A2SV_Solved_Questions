n = int(input())

inputs = []
for i in range(n):
    inputs.append(input())

for line in inputs:
    keys = set()
    passed = True
    for i in line:
        if i.islower():
            keys.add(i)
        elif i.isupper():
            if i.lower() not in keys:
                passed = False
                break   
    
    if passed:
        print("YES")    
    else:
        print("NO")




   