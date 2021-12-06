class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited=[0]*(n)
        def dfs(i):
            visited[i]=1
            for room in rooms[i]:
                if visited[room]==0:
                    dfs(room)
        dfs(0)
        return True if len(set(visited))==1 else False