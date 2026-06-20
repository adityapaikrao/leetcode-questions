class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
        counts = {} # server -> req count

        [0, 0, 0] # end_times of current load

        - request arrives:
            i = i % k
            j = i
            traverse until jth server free: assign to that
            increase count
         
        """
        n = len(arrival)

        server_counts = [0] * k
        busy_servers = [] # min heap of end times (end_times, server)
        free_servers = list(range(k)) # min heap of free servers
        heapq.heapify(free_servers)

        for curr_server, (arrival_time, load_time) in enumerate(zip(arrival, load)):
            # free up servers that can be used now
            while busy_servers and busy_servers[0][0] <= arrival_time:
                _, free_server = heapq.heappop(busy_servers)
                # push into free based on how far the freed server is from current request's preferred
                heapq.heappush(free_servers, (curr_server + (free_server - curr_server + k) % k))
            
            if free_servers:
                circular_index = heapq.heappop(free_servers)
                server_id = circular_index % k

                server_counts[server_id] += 1
                heapq.heappush(busy_servers, (arrival_time + load_time, server_id))
            
        max_requests = max(server_counts)
        return [index for index, counts in enumerate(server_counts) if counts == max_requests]

            



                