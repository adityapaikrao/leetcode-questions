class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}
        def path_sum(row_idx: int, col_idx: int) -> int:
            if (row_idx, col_idx) in memo:
                return memo[(row_idx, col_idx)]

            if col_idx >= n or col_idx < 0: 
                return float('inf')
            if row_idx == n:
                return 0
            
            
            curr_sum = matrix[row_idx][col_idx] 
            next_max = min(
                path_sum(row_idx + 1, col_idx - 1),
                path_sum(row_idx + 1, col_idx + 1),
                path_sum(row_idx + 1, col_idx)
            )
            memo[(row_idx, col_idx)] = curr_sum + next_max
            return memo[(row_idx, col_idx)]
        
        return min(path_sum(0, j) for j in range(n))


            
