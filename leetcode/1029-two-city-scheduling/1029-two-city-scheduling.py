class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        dif = []

        for i,j in costs:
            d = abs(i-j)
            dif.append([i,j,d])

        dif.sort(key = lambda x: -x[2] )
        print(dif)

        a_c = 0
        b_c = 0
        res = 0
        for i,j,d in dif:
            if i < j:
                mn = i
                a_c += 1
            else:
                mn = j
                b_c += 1
            res += mn
            print(mn)

            if a_c >= len(costs)//2 or b_c >= len(costs)//2:
                break
     
        for i,j,d in dif[a_c + b_c:] :
            if a_c < b_c:
                res += i
                print(i)
            else:
                res += j
                print(j)


        return res


            




        
        