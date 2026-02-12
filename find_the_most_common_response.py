class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        
        counter_dict = {}
        for i in range(len(responses)):
            sett = set()
            for j in responses[i]:
                if j not in sett:
                    sett.add(j)
                    counter_dict[j] = counter_dict.get(j,0) + 1

        res = []
        max_response = max(counter_dict.values())

        for i in counter_dict:
            if counter_dict[i] == max_response:
                res.append(i)

        return sorted(res)[0]


        
