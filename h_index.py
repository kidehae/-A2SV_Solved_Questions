class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        print(citations)
        h = 1
        h_list = []
        for i in range(len(citations)):
            
            if citations[i] < h:
                break
            h_list.append(h)
            h += 1
            
        if h_list:
            return max(h_list)
        else:
            return 0

            

        


        
