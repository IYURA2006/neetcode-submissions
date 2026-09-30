import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = 0

        processes = []
        available_tasks = []
        res = []

        for i in range(len(tasks)):
            start, proccessing_time = tasks[i][0], tasks[i][1]
            heapq.heappush(processes, (start, proccessing_time, i))


        while len(processes) > 0 or len(available_tasks) > 0:
            if len(available_tasks) > 0:
                t, index = heapq.heappop(available_tasks)
                res.append(index)
                time += t

            if len(processes) > 0:
                if time < processes[0][0]:
                    time = processes[0][0]

                while len(processes) > 0 and time >= processes[0][0]:
                    next_available, processing, i = heapq.heappop(processes)
                    heapq.heappush(available_tasks, (processing,i))
            
        return res