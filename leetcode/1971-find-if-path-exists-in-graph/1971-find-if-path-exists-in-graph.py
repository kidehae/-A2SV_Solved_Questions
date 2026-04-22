class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        def dfs (node, sett):
            if node == destination:
                return True

            sett.add(node)

            for i in graphs[node]:
                if i not in sett:
                    res = dfs(i,sett)
                    if res:
                        return True

            return False

        graphs = defaultdict(list)
        sett = set()
        for i,j in edges:
            graphs[i].append(j)
            graphs[j].append(i)

        return dfs(source,sett)
