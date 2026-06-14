class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        right -> down -> left -> up
        """
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        spiral_order = []

        while top <= bottom and left <= right:
            # go right
            for j in range(left, right + 1):
                spiral_order.append(matrix[top][j])
            top += 1

            if top > bottom:
                break

            # go down
            for i in range(top, bottom + 1):
                spiral_order.append(matrix[i][right])
            right -= 1

            if left > right:
                break
            
            # go left
            for j in range(right, left - 1, -1):
                spiral_order.append(matrix[bottom][j])
            bottom -= 1

            if top > bottom:
                break

            # go up
            for i in range(bottom, top - 1, -1):
                spiral_order.append(matrix[i][left])
            left += 1
        
        return spiral_order
