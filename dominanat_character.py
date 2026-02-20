t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    flag = True
    for i in range(2,8):
        for j in range(n - i + 1):
            sub_str = s[j: j+i]
            if sub_str.count("a") > sub_str.count("b") and sub_str.count("a") > sub_str.count("c"):
                flag = False
                print(i)
                break
        else:
            continue
        break
    
    if flag:
        print(-1)
