var memo = func() []int{
    m := make([]int, 46)
    m[0] = 1
    m[1] = 1
    return m
}()

func climbStairs(n int) int {
    if memo[n] != 0{
        return memo[n]
    }

    // Base Case:
    if n <= 1 {
        return 1
    }

    // Recursive Case
    memo[n] = climbStairs(n-2) + climbStairs(n-1)
    return memo[n]
}