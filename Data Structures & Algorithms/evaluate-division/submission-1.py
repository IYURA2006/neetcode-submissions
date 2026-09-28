from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        connections = defaultdict(list)
        for i in range (len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            val = values[i]

            connections[a].append((b, val))
            connections[b].append((a, 1/val))

        visited = set()
        
        def multiplicator(a, b, res):
            if a == b:
                return res

            visited.add(a)

            for neighbour, weight in connections[a]:
                if neighbour not in visited:
                    result = multiplicator(neighbour, b, res * weight)

                    #so we dont give up too early
                    if result != -1.0:

                        return result
                    
            return -1.0
        res = []
        for a,b in queries:
            if a in connections and b in connections:
                val = multiplicator(a, b, 1)
                res.append(val)
                visited.clear()
            else:
                res.append(-1)
        
        return res
            