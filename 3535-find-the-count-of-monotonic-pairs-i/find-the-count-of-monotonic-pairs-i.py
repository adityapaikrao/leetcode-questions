class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        """
        [2, 3, 2]

        [0, 1, 2] non-decreasing
        [2, 2, 0] non-increasing

        - keep track of prev nums for each array
        - for all possible arr1 nums:
            - see if arr2 num satisfies
        
        num1 >= prev1 
        num2 <= prev2 

        prev1 + prev2 = nums[i-1] => p2 = nums[i-1] - p1
        num1 >= prev1 
        & nums[i] - num1 <= nums[i-1] - prev1
        => nums[i] - nums[i-1] <= num1 - prev1 
        """
        n = len(nums)
        MOD = 10 ** 9 + 7
        memo = {}

        def find_pair(index: int, prev: int):
            if (index, prev) in memo:
                return memo[(index, prev)]

            if index == n:
                return 1
            if index != 0:
                low = max(prev, prev + nums[index] - nums[index - 1])
            else:
                low = 0
            
            count = 0
            for num1 in range(low, nums[index] + 1):
                count += find_pair(index + 1, num1)
            
            memo[(index, prev)] = count % MOD
            return memo[(index, prev)]
        

        return find_pair(0, 0) % MOD