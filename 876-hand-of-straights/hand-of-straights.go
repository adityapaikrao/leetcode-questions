/*

1 2 2 3 3 4 6 7 8
*/

import (
    "sort"
)

func isNStraightHand(hand []int, groupSize int) bool {
    if len(hand) % groupSize != 0 {
        return false
    }

    numCounts := make(map[int]int, len(hand))
    for _, num := range hand{
        numCounts[num]++
    }

    sort.Ints(hand)

    for _, num := range hand{
        if numCounts[num] == 0 {continue}

        size := 0
        currNum := num
        for size < groupSize{
            if numCounts[currNum] == 0{
                return false
            }
            numCounts[currNum]--
            currNum++
            size++
        }
    }
    return true
    
}