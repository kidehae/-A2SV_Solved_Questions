class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = True
        col = False
        row_reverse = False
        col_reverse = False

        while matrix and matrix[0]:
            if row and not row_reverse:
                rows =  matrix[0]
                res.extend(rows)
                matrix.pop(0)
                row = False
                col = True
                row_reverse = True
                



            elif row and row_reverse:
                rows =  matrix[-1]
                res.extend(rows[::-1])
                matrix.pop()
                row = False
                col = True
                row_reverse = False
                

            elif col and not col_reverse:
                for i in range(len(matrix)):
                    res.append(matrix[i].pop())
                    
                matrix = [row for row in matrix if row]
                row = True
                col = False
                col_reverse = True
            else:
                for i in range(len(matrix)-1, -1, -1):
                    res.append(matrix[i].pop(0))

                matrix = [row for row in matrix if row]
                row = True
                col = False
                col_reverse = False

        return res






            
            

        
