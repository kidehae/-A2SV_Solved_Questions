s = input()

stack = [-1]
mx = 0
cnt = 0

for i, ch in enumerate(s):
    if ch == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]

            if length > mx:
                mx = length
                cnt = 1
            elif length == mx:
                cnt += 1

if mx == 0:
    print(0, 1)
else:
    print(mx, cnt)