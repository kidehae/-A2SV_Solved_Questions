n = int(input())
for _ in range(n):
    s = input()
    functional = set()
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 2
        else:
            functional.add(s[i])
            i += 1
    
    print(''.join(sorted(functional)))
