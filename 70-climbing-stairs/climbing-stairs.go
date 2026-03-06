func climbStairs(n int) int {
   if n <= 1{
    return 1
   }

   prev1, prev2 := 1, 1
   for range n {
        prev1, prev2 = prev2, prev1 + prev2
   }
   return prev1
}