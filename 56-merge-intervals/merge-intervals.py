class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        [[1,6],[8,10],[15,18],[15,18]]
                        p
                                      i
        if overlap:
            p[1] = max(endtimes)
        else:
            p++
            p = i
        
            
        """
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key = lambda x : x[0])
        prev = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[prev][1]:
                intervals[prev][1] = max(intervals[prev][1], intervals[i][1])
            else:
                prev += 1
                intervals[prev] = intervals[i]
        return intervals[:prev + 1]
        