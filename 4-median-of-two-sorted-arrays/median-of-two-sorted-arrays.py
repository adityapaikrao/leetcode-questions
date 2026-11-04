class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        [1, 3] [2, 4]. -> [1, 2, 3, 4] median -> (2 + 3) / 2 = 2.5
        merge into one array
        sort
        get median arr[n // 2] if n odd else mean of arr[n // 2] & arr[n // 2 - 1]
        O(n + m) O(L log L) where L = n + m
         l       r
        [1, 3] [2, 4]
         l1
            r1
                l2 
                    r2
        l1 = largest num from array 1 in left half
        l2 = largest num from array 2 in left half
        r1 = smallest num from array1 in right 
        r2 = smallest nume from array2 in right
        => median = [max(l1, l2) + min(r1, r2)] / 2

        1 num from l => rest from r in the left half

        [1, 2,| 3, 4]
            l1
              r1
        [1, 2]  [3]
              l2 r2
        [1, 2, 3]
        median = max(l1, l2)  l2=-inf

        need to decide how many elems from n1 in left 
        try all possible values

        lets say n1 < n2:
            0 to M where M n1 + n2 // 2
    
            l1. r1
        [2, 3, 5]  [0, 1, 6]
                    l2  r2
        
        l1 <= r2 && l2 <= r1
        [0, 1, 2] [3, 5, 6]
        
        if l1 > r2: choose less from n1
        if l2 > r1: choose less from n2 / choose more from n1

        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        low = 0
        half = (n1 + n2) // 2
        high = min(n1, half)

        while low <= high:
            mid1 = (low + high) // 2 # nums from n1 in left half
            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < n1 else float('inf')

            mid2 = half - mid1
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < n2 else float('inf')

            if l1 > r2:
                high = mid1 - 1
            elif l2 > r1:
                low = mid1 + 1
            else:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
        

