/*
(2, 3) (5, 4) (6, 5) (6, 7)

3 5 6
         4
*/

import (
    "slices"
    "cmp"
    "fmt"
)

func maxEnvelopes(envelopes [][]int) int {
    slices.SortFunc(envelopes, func(x, y []int) int {
        if x[0] != y[0] {
            return cmp.Compare(x[0], y[0])
        }
        // descending height when widths equal
        return cmp.Compare(y[1], x[1])
    })

    seq := make([]int, 0)
    for i := range(len(envelopes)) {
        if len(seq) == 0 || envelopes[i][1] > seq[len(seq) - 1]{
            // empty or increasing seq
            seq = append(seq, envelopes[i][1])
        }

        low := 0
        high := len(seq) - 1

        for low <= high{
            mid := low + (high - low) / 2
            if seq[mid] >= envelopes[i][1]{
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        seq[low] = envelopes[i][1]
    }

    return len(seq)
}