class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        num_str = []

        for i in nums:
            num_str.extend(list(map(int, (str(i)))))

        return num_str

        
