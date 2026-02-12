class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t = [[0 for j in matrix] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                t[j][i] = matrix[i][j]
        return t

        
