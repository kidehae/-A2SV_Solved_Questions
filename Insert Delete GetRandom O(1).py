class RandomizedSet:

    def __init__(self):

        self.Sett = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.Sett:
             self.Sett.add(val)
             return True
        else:
             return False

    def remove(self, val: int) -> bool:
        if val in self.Sett:
             self.Sett.remove(val)
             return True
        else:
             return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.Sett))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
