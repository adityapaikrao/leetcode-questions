import (
    "slices"
)

func checkInclusion(s1 string, s2 string) bool {
    s1Freq := make([]int, 26)
    for i := range s1 {
        s1Freq[int(s1[i]) - int('a')]++
    }

    currFreq := make([]int, 26)
    i := 0
    j := 0

    for j < len(s2) {
        currFreq[int(s2[j]) - int('a')]++
        if j - i + 1 < len(s1) {
            j++
            continue
        } 
        
        if slices.Equal(s1Freq, currFreq) {
            return true
        }

        currFreq[int(s2[i]) - int('a')]--
        i++
        j++
    } 

    return false
}