/*

A A B A B B B
    i
              j

freq = {A:1, B:3}

at each length see k used = length - maxChar
if greater pop from front until
*/

func characterReplacement(s string, k int) int {
    freq := make([]int, 26)
    i := 0
    j := 0
    maxLen := k

    var isWindowValid func(start, end int) (bool)
    
    isWindowValid = func(start, end int) (bool) {
        maxFreq := 0
        for i := range freq {
            if freq[i] > maxFreq {maxFreq = freq[i]}
        }
        return end - start + 1 - maxFreq <= k
    }

    for j < len(s) {
        freq[int(s[j]) - int('A')]++
        // fmt.Println(i, j, freq)
        if isWindowValid(i, j){
            j++
        } else {
            maxLen = max(maxLen, j - i)
            for !isWindowValid(i, j) {
                freq[int(s[i]) - int('A')]--
                i++
            }
            j++
        }
    } 

    maxLen = max(maxLen, j - i)

    return maxLen
}