n, k, q = map(int, input().split())
recipes = []
quires = []
for i in range(n):
   recipes.append(list(map(int, input().split())))
for i in range(q):
   quires.append(list(map(int, input().split())))

diff_arr = [0] * 200001
for l, r in recipes:
   diff_arr[l] += 1
   if r + 1 < 200001: diff_arr[r + 1] -= 1 

val = 0
for i in range(200001):
   val += diff_arr[i]
   diff_arr[i] = val

arr = [0] * 200001

for i in range(200001):
   if diff_arr[i] >= k:
      arr[i] += 1

summ = 0
for i in range(200001):
   summ += arr[i]
   arr[i] = summ

res = []

for l, r in quires:
   res.append(arr[r] - arr[l - 1]) 

for i in res:
   print(i)