class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        lonely = []
        for num, count in freq.items():
            if count == 1 and (num - 1) not in freq and (num + 1) not in freq:
                lonely.append(num)
        
        return lonely