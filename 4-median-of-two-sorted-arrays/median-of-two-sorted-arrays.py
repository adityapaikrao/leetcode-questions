class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        [1 3]  & [2] -> [1, 2, 3] median = 2 ->
        [1, 2] [3, 4] -> [1, 2, 3, 4] median = (2 + 3) / 2 = 2.5
        TC: O(N + M) & SC: O(N + M)

        Better:
        median divides the array into two halves -> left (L) & right (R)
        conditions:
            - for every x in L and y in R: x <= y
            - if L + R is even: median = (max in L + min in R) / 2
            - if L + R is odd if L > R: median = max in L or if R > L: median = min in R 
                    [1] [2, 3] vs [1, 2] [3]
        Goal => need to find min max in L & R
        - some elems in L come from n1 & others come from n2
        - if we know #elems from n1 & #elems from n2 then we know min max in L
            - min = min(min in n1_left, min in n2_left)
            same for max & same for right half
        
        Assume n1 < n2:
        suppose k nums come in L from n1 
        then (half - k) come from n2 where half = (n1 + n2) // 2 i.e we keep len(L) <= len(R)

        Goal => find k 
        k between [0, len(n1)] -> do binary search on this
                                      L  R
        [1, 3, 5] [2, 4, 6] -> [1, 2, 3, 4, 5, 6] => k = 2
        suppose k = 1  => [1, 2, 4] [3, 5, 6] invalid 
        how to validate?
            l1 = index of max elem in n1 in L
            r1 = index of min elem in n1 in R
            l2, r2
                          l2
                            r2
            [1, 3, 5] [2, 4, 6]
            l1
                r1

            to be valid l1 < r2 && r1 > l2
                l1 < r2? (1 < 6) yes
                r1 > l2? (3 > 4) no => invalid 
                => r1 has to be in left => need to take more elems from n1 in L
                so move try higher value of k 
                              l2 r2
            if k = 3.  [1, 3, 5] [2, 4, 6]
                              l1
                                 r1
                l1 < r2? (5 < 2) no => try lower value of k
                r1 > l2? (inf > -inf) yes 
                  if li goes out of bounds = -inf if ri goes out of bound = +inf
                l2 r2
        [3] [2, 5, 6]
    l1
        r1
        half = 2
        """
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            # keep n1 the smaller array for consistency
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        k_min = 0
        k_max = n1
        half = (n1 + n2) // 2

        while k_min <= k_max:
            mid = (k_min + k_max) // 2
            r1 = nums1[mid] if mid < n1 else float('inf')
            l1 = nums1[mid - 1] if mid > 0 else float('-inf')

            r2 = nums2[half - mid] if half - mid < n2 else float('inf')
            l2 = nums2[half - mid - 1] if half - mid - 1 >= 0 else float('-inf')

            if r1 < l2:
                k_min = mid + 1
                continue
            elif r2 < l1:
                k_max = mid - 1
                continue
            
            if (n1 + n2) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return min(r1, r2)
        
        return 0