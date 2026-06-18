class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        
        task_counts = [-val for val in counts.values()]
        heapq.heapify(task_counts)
        time = 0
        
        while task_counts:
            temp = []
            curr_tasks = 0
            for _ in range(n + 1):
                if not task_counts:
                    break
                count = heapq.heappop(task_counts)
                count += 1
                if count < 0: temp.append(count)
                curr_tasks += 1
            
            while temp:
                heapq.heappush(task_counts, temp.pop())

            time += n + 1 if task_counts else curr_tasks
        return time

