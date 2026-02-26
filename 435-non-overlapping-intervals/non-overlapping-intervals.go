import (
    "sort"
)

func eraseOverlapIntervals(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool{
        return intervals[i][0] < intervals[j][0]
    })

    i := 0
    count := 0
    for j := 1; j < len(intervals); j++{
        if intervals[i][1] > intervals[j][0]{
            if intervals[i][1] > intervals[j][1]{
                i = j
            }
            count++
        } else {
            i = j
        }
    }

    return count
}