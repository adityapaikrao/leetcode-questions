class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ready_tasks = [] # max heap of process at (count, task)
        blocked_tasks = [] # min heap of blocked tasks (time, task)

        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        for task, count in counts.items():
            heapq.heappush(ready_tasks, (-count, task))
        
        time = 0
        while blocked_tasks or ready_tasks:
            # check if new tasks are available now
            while blocked_tasks and blocked_tasks[0][0] <= time:
                _, task = heapq.heappop(blocked_tasks)
                heapq.heappush(ready_tasks, (-counts[task], task))
            
            # print(time, ready_tasks, blocked_tasks, counts)
            if ready_tasks:
                _, task = heapq.heappop(ready_tasks)
                counts[task] -= 1
                if counts[task] > 0:
                    heapq.heappush(blocked_tasks, (time + n + 1, task))

            time += 1
        
        return time

            
