class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        all_combs = []
        curr_comb = [["."] * n for _ in range(n)]

        def valid_placement(row_idx: int, col_idx: int) -> bool:
            if any(curr_comb[i][col_idx] == "Q" for i in range(row_idx)):
                return False
            
            if any(curr_comb[row_idx][j] == "Q" for j in range(col_idx)):
                return False
            
            i, j = row_idx - 1, col_idx - 1
            while i >= 0 and j >= 0:
                if curr_comb[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            i, j = row_idx + 1, col_idx - 1
            while i < n and j >= 0:
                if curr_comb[i][j] == "Q":
                    return False
                i += 1
                j -= 1
            
            return True
        
        def find_placements(col_idx: int) -> None:
            # Out of Bounds
            if col_idx >= n:
                copy = curr_comb
                all_combs.append(["".join(row[:]) for row in copy])
                return 
            
            # place queens column wise
            for row_idx in range(n):
                if valid_placement(row_idx, col_idx):
                    curr_comb[row_idx][col_idx] = "Q"
                    find_placements(col_idx + 1)
                    curr_comb[row_idx][col_idx] = "."
            return
        
        find_placements(0)

        return all_combs


