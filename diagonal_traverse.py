class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        nums_counter = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                nums_counter[i + j].append(mat[i][j])
        
        res = []
        for i in nums_counter:
            if i % 2 == 0:
                res.extend(nums_counter[i][::-1])
            else:
                res.extend(nums_counter[i])

        return res


        
