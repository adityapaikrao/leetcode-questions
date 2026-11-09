class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        """
        k = 3 => 3 servers

        s0 s1 s2   

        counts = {s0: 1, s1: 2, s2: 1}

        free = [] busy = [(s0, 6), (s2, 6), (s1, 7)]

                    i
        1, 2, 3, 4, 5 arrival time
        5, 2, 3, 3, 3 load

        need a way to order free heap by servers in the preference order 
        (j - i + k)

        i = 1 order = s1 s2 s0.  {1 -> 3, 2 -> 1, 3-> 1}
        i = 2 order = s2 s0 s1

        so when pushed in busy push with (time, server_idx)
        when popped from busy & pushed into free: push with (preferred_idx, idx)

        preferred_idx = (server_idx - i) % k = r
        """
        counts = [0] * k

        free = [i for i in range(k)]
        busy = []

        for i, (arrival_time, req_load) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arrival_time:
                _, server_idx = heapq.heappop(busy)
                heapq.heappush(free, i + (server_idx - i) % k)
            
            if free:
                idx = heapq.heappop(free)
                counts[idx % k] += 1
                heapq.heappush(busy, (arrival_time + req_load, idx % k))
        
        max_val = max(counts)
        return [idx for idx, count in enumerate(counts) if count == max_val]

