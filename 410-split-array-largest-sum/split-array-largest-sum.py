class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        [7, 2, 5, 10, 8] k = 2

        low = min(nums)
        high = sum(nums)
        """
        if k == 1:
            return sum(nums)
        
        def isPossible(mid: int, k: int) -> bool:
            curr_sum = 0
            count = 1

            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    curr_sum = num
                    count += 1
            
            return count <= k
    
        low = max(nums)
        high = sum(nums)

        min_sum = high

        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid, k):
                min_sum = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return min_sum


