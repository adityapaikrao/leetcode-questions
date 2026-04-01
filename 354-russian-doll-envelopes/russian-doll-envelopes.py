class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        order by widths: [2, 3] [5, 4] [6, 4] [6, 7]
        order by heights: [2, 3] [5, 4] [6, 4] [6, 7]

        - essentially need to find LIS where widths & height both strictly increasing 
        - but how do we combine two dimensions?

        within same width group only 1 envelope can be chosen in the LIS of heights
            - order by width ASC, height DESC to ensure this
        
        [1, 3, 2, 5]

        seq = [1, 2, 3]
                 
        """
        envelopes.sort(key = lambda x : (x[0], -x[1]))

        seq = []

        for _, height in envelopes:
            if not seq or seq[-1] < height:
                seq.append(height)
                continue
            
            i, j = 0, len(seq) - 1
            while i <= j:
                mid = (i + j) // 2
                if seq[mid] < height:
                    i = mid + 1
                else:
                    j = mid - 1

            seq[i] = height
        
        return len(seq)