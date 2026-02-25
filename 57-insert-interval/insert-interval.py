class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        while i < n:
            if intervals[i][0] > newInterval[1]:
                # print("cond2")
                new_intervals = intervals[:i]
                new_intervals.append(newInterval)
                new_intervals.extend(intervals[i:])
                return new_intervals
            if intervals[i][1] >= newInterval[0]:
                # print(f"cond1 {intervals[i]} && {newInterval}")
                intervals[i][1] = max(intervals[i][1], newInterval[1])
                intervals[i][0] = min(intervals[i][0], newInterval[0])
                break
            i += 1
        
        # print(intervals)
        if i == n:
            intervals.append(newInterval)
            return intervals
        else:
            j = i 
            while j < n and intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j += 1
            # print(f"j: {j} && {intervals[j]}")
            new_intervals = intervals[:i+1]
            new_intervals.extend(intervals[j:])
        
            return new_intervals
                
            

            
            

        
            
            