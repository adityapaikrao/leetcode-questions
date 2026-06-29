class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        seen = set()
        for val in freq.values():
            if val in seen:
                return False
            seen.add(val)
        
        return True
