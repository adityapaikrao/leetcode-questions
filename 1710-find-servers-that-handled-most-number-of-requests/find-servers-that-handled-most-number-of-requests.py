from collections import defaultdict
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        """
        k servers
        for ith request -> (i % k) th server or next available server (circular wrapping)

        (arrival_time, request_load)_i 
        arrival_time_i < arrival_time_j for all i < j

        find busiest server

        map: server_counts = {}
        end_times for servers: List / heap

        [(1, 5), (2, 2), (3, 3), (4, 3), (5, 3)]
                                   i

        end_times: [5, 4, 6] 
        available: []
        map: [1, 1, 1]

        request comes in (a, l):
            update available servers:
                - if a >= end_time: put into available servers
                - push flag based on how far available srver is from current's pref
                    - curr + (avail - curr + k) % k
                     0 + (1 - 0) % 3 => 1
                     5 + (1 - 5) % 3 => 5 + 2 => 7 7 % 3 => 1


            check if (i % k)th server available
            update end time to a + l

            if available servers:
                pop from top & recover orginal index by %k

        """
        available = [i for i in range(k)]
        end_times = [] # (time, server_idx)
        counts = [0] * k
        heapq.heapify(available)

        for index, request in enumerate(zip(arrival, load)):
            preferred = index % k
            # print(end_times, available)

            while end_times and end_times[0][0] <= request[0]:
                _, new_server = heapq.heappop(end_times)
                new_idx = index + (new_server - index) % k
                heapq.heappush(available, new_idx)
            
            if available:
                server_idx = heapq.heappop(available) % k
                counts[server_idx] += 1
                
                # update end time for new task
                heapq.heappush(end_times, (request[0] + request[1], server_idx))
        # print(counts)
        max_count = max(counts)
        return [server_idx for server_idx, count in enumerate(counts) if count == max_count]