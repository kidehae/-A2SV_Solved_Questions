class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        crcs = defaultdict(list)


        def dfs(crs):
            if crs in sett:
                return False
            if crcs[crs] == []:
                return True

            sett.add(crs)
            for i in crcs[crs]:
                if not dfs(i):
                    return False

            sett.remove(crs)
            crcs[crs] = []
            return True



        for k,v in prerequisites:
            crcs[k].append(v)

        sett = set()
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




    
        