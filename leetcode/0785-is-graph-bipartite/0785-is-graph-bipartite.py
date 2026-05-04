class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        grps = [-1] * (len(graph))
        res = True

        def dfs(i):
            temp = True
            for j in graph[i]:
                if grps[j] == -1:
                    if grps[i] == 0:
                        grps[j] = 1
                    else:
                        grps[j] = 0
                    temp = temp and dfs(j)

                elif grps[i] == grps[j]:
                    return False

            return temp


        for i in range(len(graph)):
            if grps[i] == -1:
                grps[i] = 0
                res = res and dfs(i)

        return res

        