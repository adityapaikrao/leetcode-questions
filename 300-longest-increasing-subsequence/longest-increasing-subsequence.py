class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return 1
        
        seq = []
        
        for num in nums:
            if not seq or num > seq[-1]:
                seq.append(num)
            else:
                low = 0
                high = len(seq) - 1

                while low <= high:
                    mid = low + (high - low) // 2
                    if num > seq[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
                
                seq[low] = num
        return len(seq)