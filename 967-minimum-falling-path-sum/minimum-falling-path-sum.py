class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(n - 2, -1, -1):
            for j in range(n):
                matrix[i][j] += min(
                    matrix[i + 1][j-1] if j >= 1 else float('inf'),
                    matrix[i + 1][j],
                    matrix[i + 1][j+1] if j < n - 1 else float('inf')
                )

        return min(matrix[0][j] for j in range(n))