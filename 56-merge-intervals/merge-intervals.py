class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1, 6], [8, 10], [15, 18], [2, 6]]
                            p
                                      i
        
        [1, 3] [4, 5]
                p
                i

        """
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[prev][1] >= intervals[i][0]:
                intervals[prev][1] = max(intervals[prev][1], intervals[i][1]) 
            else:
                prev += 1
                if prev != i: intervals[prev], intervals[i] = intervals[i], intervals[prev]

        return intervals[:prev + 1] 
