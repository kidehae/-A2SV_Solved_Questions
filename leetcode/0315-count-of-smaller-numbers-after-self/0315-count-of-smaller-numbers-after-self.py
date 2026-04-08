class Solution:
    def countSmaller(self, nums):
        ans = [0] * len(nums)

        def merge(left, right):
            l, r = 0, 0
            res = []
            right_count = 0 

            while l < len(left) and r < len(right):
                if left[l][0] <= right[r][0]:
                    ans[left[l][1]] += right_count
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    right_count += 1
                    r += 1

            while l < len(left):
                ans[left[l][1]] += right_count
                res.append(left[l])
                l += 1

            while r < len(right):
                res.append(right[r])
                r += 1

            return res

        def mergesort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left, right)

        arr = [(nums[i], i) for i in range(len(nums))]
        mergesort(arr)

        return ans




