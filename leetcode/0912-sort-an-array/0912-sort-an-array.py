class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):

            l, r = 0, 0
            res = []
            while l < len(left) and r < len(right):

                if left[l] < right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1

            res.extend(left[l:])
            res.extend(right[r:])
            return res

        def mergesort(left, right, arr):
            if left == right:
                return [arr[left]]

            mid = left + (right - left) // 2
            left_part = mergesort(left, mid, arr)
            right_part = mergesort(mid + 1, right, arr)

            return merge(left_part,right_part )

        return mergesort(0, len(nums)-1, nums)





