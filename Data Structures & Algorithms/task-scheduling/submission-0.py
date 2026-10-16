import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # X X X Y Y Z
        task_freq = {task : 0 for task in tasks}
        for task in tasks:
            task_freq[task] += 1
        
        queue = []

        for task, freq in task_freq.items():
            queue.append((-freq, task))
        
        print(queue)
        time = 0

        
        while queue:
            to_be_back = []
            for layer in range(n + 1):
                if not queue and not to_be_back:
                    break
                
                if not queue:
                    time += 1
                    continue
           
                freq, item = heapq.heappop(queue)
                freq += 1

                if freq != 0:
                    to_be_back.append((freq, item))

                time += 1

            for item in to_be_back:
                heapq.heappush(queue, item)
        
        return time
