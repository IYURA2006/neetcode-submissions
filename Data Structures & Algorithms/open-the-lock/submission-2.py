from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 0 0 0 0
        # 1 0 0 0 '  0 1 0 0 '  0 0 1 0 ' 0 0 0 1 '
        # 
        start_state = list("0000")
        deadends = set(deadends)

        if "".join(start_state) in deadends:
            return -1 
        visited = set()

        def helper(lock):
            queue = deque()
            queue.append(lock)
            visited.add("".join(lock))
            turns = 0

            while queue:
                for _ in range(len(queue)):
                    cur_state = queue.popleft()
                    matching_format = "".join(cur_state)
               
                    if matching_format == target:
                        return turns

                    else: 

                        #up
                        for i in range(4):
                            new_combo = cur_state.copy()
                            new_combo[i] = str( (int(new_combo[i]) + 1) % 10)

                            new_combo_str = "".join(new_combo)
                            if new_combo_str not in deadends and new_combo_str not in visited:
                                queue.append(new_combo)
                                visited.add("".join(new_combo))

                        #down
                        for i in range(4):
                            new_combo = cur_state.copy()
                            new_combo[i] = str( (int(new_combo[i]) - 1 ) % 10)
                       

                            new_combo_str = "".join(new_combo)
                            if new_combo_str not in deadends and new_combo_str not in visited:
                                queue.append(new_combo)
                                visited.add("".join(new_combo))


        
                turns += 1
            return -1
        return helper(start_state)


