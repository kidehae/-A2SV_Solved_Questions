class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk  = []
        for i in logs:
            if stk and i == "../":
                stk.pop()
            elif i != "./" and i != "../" :
                stk.append(i)
        
        return len(stk)