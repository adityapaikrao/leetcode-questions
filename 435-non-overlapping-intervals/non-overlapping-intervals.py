class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [1,2] [1,3] [2,3], [3, 4]
        
        0 -> 1
        1 -> 0, 2
        2 -> 1
        3 -> 
        """
        if len(intervals) <= 1:
            return 0

        intervals.sort()
        count = 0

        i = 0
        for j in range(1, len(intervals)):
            if intervals[i][1] > intervals[j][0]:
                # overlap
                if intervals[i][1] > intervals[j][1]:
                    # remove the ith intervals since it has a later end time
                    i = j
                    count += 1
                else:
                    count += 1
            else:
                i = j
        
        return count
