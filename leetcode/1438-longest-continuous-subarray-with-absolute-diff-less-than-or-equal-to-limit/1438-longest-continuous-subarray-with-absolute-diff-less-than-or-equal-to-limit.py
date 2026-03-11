class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        max_width = 0

        for i , val in enumerate(nums):

            while inc and abs(inc[0][0] - val) > limit:
                inc.popleft()

            while dec and abs(dec[0][0] - val) > limit:
                dec.popleft()
            mn, mx = i, i
            
        
            while inc and inc[-1][0] > val:
                mn = inc[-1][1]
                inc.pop()

            while dec and dec[-1][0] < val:
                mx = dec[-1][1]
                dec.pop()

            inc.append(tuple([val, mn]))
            dec.append(tuple([val, mx]))

            min_side = min(i - inc[0][1] + 1, i - dec[0][1] + 1)
            max_width = max(max_width,min_side )

        return max_width


            
            


        