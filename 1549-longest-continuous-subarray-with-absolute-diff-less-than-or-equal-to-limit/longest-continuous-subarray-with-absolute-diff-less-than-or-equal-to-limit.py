"""
10, 1, 2, 4, 7, 2
                i
       s

limit = 4 
maxes = [7, 4, 2, 2, 1] # maxheap
mins = [2, 2, 4, 10] # minheap
counts = {10:0, 1:0, 2:1, 4: 1, 7:1}

max = 7
min = 2

1. update min or max
    - push into mins/maxes, update count
    - set max to curr
    - set min to curr
2. see if valid
    - invalid: 
        - pop until valid
        - update count & remove from maxes/mins if num == max or min
        - update mins/maxes
    - push into mins & maxes
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxes, mins = [], []
        longest, start = 0, 0
        counts = defaultdict(int)

        for i in range(len(nums)):
            counts[nums[i]] += 1
            heapq.heappush(maxes, -nums[i])
            heapq.heappush(mins, nums[i])

            # remove invalid nums from max & mins; lazy deletion
            while maxes and counts[-maxes[0]] == 0:
                heapq.heappop(maxes)
            while mins and counts[mins[0]] == 0:
                heapq.heappop(mins)
            
            if -maxes[0] - mins[0] > limit:
                longest = max(longest, i - start)
                # make valid
                while -maxes[0] - mins[0] > limit:
                    counts[nums[start]] -= 1
                    if nums[start] == -maxes[0]: heapq.heappop(maxes)
                    if nums[start] == mins[0]: heapq.heappop(mins)

                    # remove invalid nums from max & mins
                    while maxes and counts[-maxes[0]] == 0:
                        heapq.heappop(maxes)
                    while mins and counts[mins[0]] == 0:
                        heapq.heappop(mins)
                    start += 1
        
        longest = max(longest, len(nums) - start)
        return longest



