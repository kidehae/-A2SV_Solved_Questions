
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
       
        n, m = len(img), len(img[0])
        new_mtrx = [[0 for j in row] for row in img]

        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(n):
            for j in range(m):
                count = 0
                for x,y in moves:
                    if n > x + i >= 0 and m > y + j >= 0:
                         new_mtrx[i][j] += img[i + x][j + y]
                         count += 1

                new_mtrx[i][j] //= count

        return new_mtrx


                


