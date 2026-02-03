class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        res = []
        kev = celsius + 273.15
        far = celsius * 1.80 + 32.00
        res.append(kev)
        res.append(far)
        return res
    


        
