import (
    "fmt"
)

func factorial(n int) int {
    if n <= 1 {
        return 1
    }
    return n * factorial(n - 1)
}

func uniquePaths(m int, n int) int {
    if m > n {
        m, n = n, m
    }

    numWays := 1
    for i := 1; i <= m - 1; i++{
        numWays = numWays * (n - 1 + i) / i
    }

    return numWays
}