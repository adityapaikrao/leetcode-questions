func insert(intervals [][]int, newInterval []int) [][]int {
    newIntervals := make([][]int, 0, len(intervals))

    // all non-overlapping intervals that end before newintervals stay as is
    i := 0
    for i < len(intervals) && intervals[i][1] < newInterval[0] {
        newIntervals = append(newIntervals, intervals[i])
        i++
    }

    // this interval overlaps with the new one, keep merging overlapping intervals
    for i < len(intervals) && intervals[i][0] <= newInterval[1] {
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i++
    }
    newIntervals = append(newIntervals, newInterval)

    // all remaining intervals remain as is
    for i < len(intervals) {
        newIntervals = append(newIntervals, intervals[i])
        i++
    }

    return newIntervals
}