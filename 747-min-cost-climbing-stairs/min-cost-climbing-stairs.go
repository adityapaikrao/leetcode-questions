func minCostClimbingStairs(cost []int) int {
    // dp := make([]int, len(cost) + 1)
    prevCost1, prevCost2 := 0, 0

    for i := 2; i < len(cost) + 1; i++{
        prevCost1, prevCost2 = min(prevCost2 + cost[i-2], prevCost1 + cost[i-1]), prevCost1
    }

    return prevCost1
}