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

        freq of each number: 1 to N
        have buckets of freq -> 
        put each number in bucket corresponding to its freq
        traverse from behind until we have k elems

        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        top_k = []
        for i in range(len(buckets) - 1, -1, -1):
            top_k.extend(buckets[i])
            if len(top_k) >= k: break
        
        return top_k[:k]
        


