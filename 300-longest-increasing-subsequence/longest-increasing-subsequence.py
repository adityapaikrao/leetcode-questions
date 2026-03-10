class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for num in nums:
            low = 0
            high = len(seq) - 1
            if not seq or seq[-1] < num:
                seq.append(num)
                continue
            
            # find smallest elem >= num
            while low <= high:
                mid = (low + high) // 2
                if seq[mid] == num:
                    low = mid
                    break
                
                if seq[mid] > num:
                    high = mid - 1
                else:
                    low = mid + 1
            
            seq[low] = num
            # print("for num:", num)
            # print(seq)
        
        return len(seq)
