class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if target > nums[-1] or target < nums[0]:
            return [-1, -1]
        
        low = 0 
        high = len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if first == -1:
            return [-1, -1]
        
        low = first
        high = len(nums) - 1
        last = first
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return [first, last]
                    