import sys
import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjlist = {i:[] for i in range(n)}
        sys.setrecursionlimit(200000)
        for m in range(len(manager)):
            if manager[m] == -1:
                continue
            adjlist[manager[m]].append((m, informTime[manager[m]]))
        
        
        visited = set()
        totaltime = 0
        def dfs(node, cur_time):
            nonlocal totaltime
            
            totaltime = max(cur_time, totaltime)

            for neighbour, time in adjlist[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour, time + cur_time)
        
                
        dfs (headID, 0)
        return totaltime

