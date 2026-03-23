class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def check (p1, l , r):
            if l > r:
                return 0
            if p1:
                p1 = not p1
                return max( nums[l] + check(p1, l + 1, r), nums[r] + check(p1, l, r - 1))
            p1 = not p1
            return min(check(p1, l + 1, r) - nums[l], check(p1, l, r - 1) - nums[r])

        if len(nums) == 1:
            return True

        return check(True, 0, len(nums) - 1) >= 0
            
            