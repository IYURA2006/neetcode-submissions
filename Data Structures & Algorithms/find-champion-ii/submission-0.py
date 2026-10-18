class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = {i:[] for i in range(n)}

        for a,b in edges:
            in_degree[b].append(a)
        
        res = None
        print(in_degree)
        for team, stronger in in_degree.items():
            if len(stronger) == 0:
                if res == None:
                    res = team
                else:
                    return -1
        return res