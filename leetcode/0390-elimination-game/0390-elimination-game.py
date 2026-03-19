class Solution:
    def lastRemaining(self, n: int) -> int:

        def elimnate(n, dir):
            if n == 1:
                return 1

            if dir == "left":
                return 2*elimnate(n // 2, "right")
            else:
                if n % 2 == 0:
                    return 2*elimnate(n // 2, "left") - 1
                else:
                    return 2*elimnate(n // 2, "left")

        return(elimnate(n,"left"))

        



        