class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        """
        [3, 3, 2]
         0  1. 2

         free = [0, 1, 2]. busy = []

                        j
        [1, 2, 3, 2, 1, 2]

        [2, 2, 0, 1, 2]

        on each task
        - add busy servers freeing up at j
        - pick up free server
        - add picked server to busy with time j + task_time
        """
        free = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free) # min heap ordered by weight & index

        busy = [] # min heap ordered by (time, serverId)
        ans = []

        curr_time = 0
        for j, task_time in enumerate(tasks):
            curr_time = max(curr_time, j)
            while busy and busy[0][0] <= curr_time:
                _, serverId = heapq.heappop(busy)
                heapq.heappush(free, (servers[serverId], serverId))
            
            if not free:
                curr_time = busy[0][0]
                while busy and busy[0][0] <= curr_time:
                    _, serverId = heapq.heappop(busy)
                    heapq.heappush(free, (servers[serverId], serverId))
            
            _, serverId = heapq.heappop(free)
            ans.append(serverId)
            heapq.heappush(busy, (curr_time + task_time, serverId))

        
        return ans




        