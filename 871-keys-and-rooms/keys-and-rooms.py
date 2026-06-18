class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        
        def dfs(room_idx: int) -> None:
            visited[room_idx] = True
            for nbr_idx in rooms[room_idx]:
                if not visited[nbr_idx]:
                    dfs(nbr_idx)

        dfs(0)
        
        return all(visited)