class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # keys = set()
        # add all elements in room[i] to keys
        # if i in keys: move forward
        # else: return False

        # keys = set()
        # keys.add(0)
        # visited = [0] * len(rooms)

        # for idx, nextkeys in enumerate(rooms):
        #     if idx not in keys:
        #         continue
        #     else:
        #         visited[idx] = 1
        #         for nextkey in nextkeys: keys.add(nextkey);
        
        # for i in range(len(visited)):
        #     if visited[i] == 0 and i in keys:
        #         visited[i] = 1
        
        # return all(visited)

        visited = set()

        def dfs(n: int):
            if n in visited:
                return 
            
            keys = rooms[n]
            visited.add(n)
            for k in keys:
                dfs(k)
        
        dfs(0)
        return len(rooms) == len(visited)

