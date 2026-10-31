class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        [100,4,200,1,3,2] -> sort [1, 2, 3, 100, 200]
                   i 
        length = 1
        max_length = max(max_length, length) # 3
        -O (Nlog N)


        first pass -> set(1, 2, 3, 100, 200)
        at each number -> try to form a consective sequ

        for num in nums:
            length = 1
            curr_num = num
            while curr_num + 1 in seen:
                length += 1
                curr_num += 1
            max_length = max(max_length, length)
 
        1 2 3 4 5 6 7 8 9 10 -> O(n^ 2)
        start with only nums that can start a seq
        each numer only processed twice -> O(n)

        """
        seen = set(nums)
        max_length = 0
        for num in nums:
            curr_num = num
            if curr_num - 1 in seen: continue

            length = 1
            while curr_num + 1 in seen:
                length += 1
                curr_num += 1
                seen.remove(curr_num)
            max_length = max(max_length, length)
        
        return max_length