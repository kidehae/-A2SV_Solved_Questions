class Solution:
    def decodeString(self, s: str) -> str:

        stck = []

        for i in s:
            if i != "]":
                stck.append(i)
            else:
                sub_str = ""
                while stck and stck[-1] != "[":
                    sub_str = stck.pop() + sub_str 
                stck.pop()

                n = ""
                
                # while stck and not(stck[-1].isalpha()):
                while stck and stck[-1].isdigit():
                
                    n = stck.pop() + n
                print(n)
                stck.append(int(n) * sub_str)

        return "".join(stck)


        