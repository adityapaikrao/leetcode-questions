import (
    "container/heap"
)

type MinHeap [][]int // time, row, col

func (h MinHeap) Len() int {return len(h)}
func (h MinHeap) Less(i, j int) bool {return h[i][0] < h[j][0]}
func (h MinHeap) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func (h *MinHeap) Push(x any) {
    *h = append(*h, x.([]int))
}
func (h *MinHeap) Pop() any {
    old := *h
    x := old[len(old) - 1]
    *h = old[:len(old) - 1]
    return x
}

func inBounds(row, col, n int) bool {
    return row >= 0 && row < n && col >= 0 && col < n
}

func swimInWater(grid [][]int) int {
    n := len(grid)
    times := make([][]int, n)
    for i := range n {
        times[i] = make([]int, n)
        for j := range n{
            times[i][j] = (1 << 31) -1
        }
    }
    times[0][0] = grid[0][0]
    h := make(MinHeap, 0)
    heap.Init(&h)
    heap.Push(&h, []int{times[0][0], 0, 0}) // time, row, col

    for len(h) > 0 {
        currPoint := heap.Pop(&h).([]int)
        if grid[currPoint[1]][currPoint[2]] == -1 { // already visited
            continue
        }
        if currPoint[1] == n - 1 && currPoint[2] == n - 1{
            break
        }

        grid[currPoint[1]][currPoint[2]] = -1 // mark as visited

        for _, offset := range [][]int{{0, -1}, {0, 1}, {1, 0}, {-1, 0}} {
            newRow := currPoint[1] + offset[0]
            newCol := currPoint[2] + offset[1]
            if inBounds(newRow, newCol, n) && grid[newRow][newCol] != -1 {
                newTime := max(grid[newRow][newCol], currPoint[0]) 
                // can reach when path opens i.e both are submerged (max of the two)
                if newTime < times[newRow][newCol] {
                    times[newRow][newCol] = newTime
                    heap.Push(&h, []int{newTime, newRow, newCol})
                }                
            }
        }

    }
    
    return times[n-1][n-1]

}