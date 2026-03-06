var memo []int

func init(){
    memo = make([]int, 46)
    memo[0] = 1
    memo[1] = 1
}

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