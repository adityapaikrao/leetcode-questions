class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        - k between 1 & N?
        - range of numbers? 
        - size of array

        counts = {1:3, 2:2, 3:1}
        sort by counts -> get top-k 
            - TC:O(N log N) SC: O(N)
        
        min heap -> (counts, num) 
        maintain heap size at most k: pop elements when size goes beyond k 
        N - k lowest elements removed => top k in heap
        """
        # get frequencies
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        min_heap = [] # (count, num)
        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k: heapq.heappop(min_heap)
        
        return [num for _, num in min_heap]