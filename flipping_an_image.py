class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])

        new_mtrx = []

        for i in range(rows):
            flip_row = image[i][::-1]
            for j in range(cols):
                if flip_row[j]== 0:
                    flip_row[j] = 1
                else:
                    flip_row[j] = 0
            new_mtrx.append(flip_row)

        return new_mtrx

    
