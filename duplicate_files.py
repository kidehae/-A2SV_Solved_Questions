class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        file_paths = []

        for i in paths:
            path = i.split()
            for i in range(1, len(path)):
                file_paths.append(path[0]+ "/"+ path[i])

        for i in file_paths:
            comp = i.split("(")
            path = comp[0]
            key = comp[1]
            contents[key].append(path)

        dup_contents = []
        for key, val in contents.items():
            if len(contents[key]) > 1:
                dup_contents.append(contents[key])

        return dup_contents







