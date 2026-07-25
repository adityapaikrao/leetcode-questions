from typing import Tuple
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def get_coords(num: int, n: int) -> Tuple[int, int]:
                # TODO: create conversion
                row = (num - 1) // n
                col = (num - 1) % n

                if row % 2 == 0:
                    return (n - 1 - row, col)
                else:
                    return (n - 1 - row, n - 1 - col)
        
        n = len(board)
        moves = 0
        frontier = deque([1])
        board[n-1][0] = n ** 2 + 1 # mark as visited
        
        while frontier:
            # print(moves, frontier)
            for _ in range(len(frontier)):
                curr_num = frontier.popleft()
                if curr_num == n ** 2:
                    return moves

                for next_num in range(curr_num + 1, min(n ** 2 + 1, curr_num + 7)):
                    next_x, next_y = get_coords(next_num, n)
                    if board[next_x][next_y] == n ** 2 + 1: continue
                    elif board[next_x][next_y] == -1: frontier.append(next_num)
                    else: frontier.append(board[next_x][next_y])
                    board[next_x][next_y] = n ** 2 + 1

            moves += 1
        
        return -1
            

