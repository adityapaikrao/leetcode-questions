// get the longest odd len palindrome containing s[i] at middle
func getOddLenPalindrome(s string, index int) (int, int) {
    left, right := index - 1, index + 1
    if left < 0 || right >= len(s) {
        return index, index
    }

    for left >= 0 && right < len(s) && s[left] == s[right]{
        left--
        right++
    }

    return left + 1, right - 1
}


// get the longest even len palindrome containing s[i] at middle
func getEvenLenPalindrome(s string, index int) (int, int) {
    left, right := index, index + 1
    if right >= len(s) {
        return index, index
    }

    for left >= 0 && right < len(s) && s[left] == s[right]{
        left--
        right++
    }

    // fmt.Println(index, left + 1, right - 1)

    return left + 1, right - 1
}


func longestPalindrome(s string) string {
    longestStart, longestEnd := 0, 0
    for i := range len(s){
        oddStart, oddEnd := getOddLenPalindrome(s, i)
        evenStart, evenEnd := getEvenLenPalindrome(s, i)
        // fmt.Println("i:", i)
        // fmt.Println("Even:", evenStart, evenEnd)
        // fmt.Println("Odd:", oddStart, oddEnd)

        if oddEnd - oddStart > longestEnd - longestStart{
            longestStart = oddStart
            longestEnd = oddEnd
        }
        if evenEnd - evenStart > longestEnd - longestStart{
            longestStart = evenStart
            longestEnd = evenEnd
        }

        // fmt.Println(longestStart, longestEnd)

    }

    return s[longestStart:longestEnd + 1]
}