class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        res = 0
        left = 0
        right = len(skill) - 1

        skill.sort()
        summ = skill[left] + skill[right]

        while left < right:
            if (skill[left] + skill[right]) == summ:
                res += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                res = -1
                break
        return res
                

        
