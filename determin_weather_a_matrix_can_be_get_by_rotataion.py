class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

        for i in range(4):
            temp = copy.deepcopy(mat)
            for j in range(len(mat)):
                temp[j] = [row[::-1][j] for row in mat]

            if temp == target:
                return True
            mat = copy.deepcopy(temp)

        return False

        
