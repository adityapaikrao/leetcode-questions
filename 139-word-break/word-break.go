func canBreak(wordSet map[string]bool, index int, s *string, memo map[int]bool) bool{
    // memoized check
    if val, ok := memo[index]; ok {
        return val
    }
    // found word
    if index == len(*s) {
        return true
    }

    // check current word
    for i := index; i < len(*s); i++{
        if !wordSet[(*s)[index: i + 1]]{
            continue
        }

        if canBreak(wordSet, i + 1, s, memo){
            memo[index] = true
            return true
        }
    }

    memo[index] = false
    return false
}

func wordBreak(s string, wordDict []string) bool {
    wordSet := make(map[string]bool)
    for _, word := range wordDict {
        wordSet[word] = true
    }

    memo := make(map[int]bool, len(s) + 1)
    return canBreak(wordSet, 0, &s, memo)

}