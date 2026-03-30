func candy(ratings []int) int {
    candies := 1
    i := 1

    for i < len(ratings) {
        for i < len(ratings) && ratings[i] == ratings[i-1]{
            candies++
            i++
        }

        peak := 1
        for i < len(ratings) && ratings[i] > ratings[i-1]{
            peak++
            candies += peak
            i++
        }

        valley := 0
        for i < len(ratings) && ratings[i] < ratings[i-1]{
            valley++
            candies += valley
            i++
        }

        if valley + 1 > peak{
            candies += valley + 1 - peak
        }
    }

    return candies
}