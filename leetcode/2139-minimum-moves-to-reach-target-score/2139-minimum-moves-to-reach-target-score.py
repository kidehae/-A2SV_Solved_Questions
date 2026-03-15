class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        steps = 0
        t = target
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target /= 2
                maxDoubles -= 1
            elif maxDoubles <= 0:
                steps += target - 1
                break
            else:
                target -= 1

            steps += 1

        return int(steps)



        