from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        

        visited = set()

        group = [-1] * len(graph)

        print(group)

        def bfs(node):
            queue = deque()
            queue.append(node)

            cur_group = 0

            while queue:

                for i in range(len(queue)):
                    item = queue.popleft()
                    group[item] = cur_group
                    
                    for neighbour in graph[item]:
                        # does not have a colour
                        if group[neighbour] == -1:
                            queue.append(neighbour)

                        #has a colour and is wrong
                        elif group[neighbour] == cur_group:
                            return False
                        
                        else:
                            pass
                        
                cur_group = 1 - cur_group
                
            return True

        for i in range(len(graph)):
            if group[i] == -1:
                if not bfs(i):
                    return False
        return True




