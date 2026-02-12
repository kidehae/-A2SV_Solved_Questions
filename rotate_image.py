class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = copy.deepcopy(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                col = len(matrix) - i - 1
                row = j
                matrix[row][col] = temp[i][j]


        
