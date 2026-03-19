t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    wins = 0
    mx = nums[-1]

    for i in range(n-1, 1, -1):
        l = 0
        for j in range(i-1, 0, -1):
            while (nums[l] + nums[j] <= nums[i] and l < j) or (nums[l]+ nums[j]+nums[i] <= mx and l < j):
                l += 1
            if l == j:
                break
            wins += j - l

    print(wins)