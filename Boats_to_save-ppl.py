class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        left = 0
        right = len(people) - 1
        boat = 0
        added  = 0

        while left < right:

          
            if people[left] + people[right] <= limit:
                boat += 1
                left += 1
                right -=1
                added += 2

                
            elif people[left] + people[right] > limit:
                right -= 1

        return boat + (len(people) - added)

            


        

        





        
