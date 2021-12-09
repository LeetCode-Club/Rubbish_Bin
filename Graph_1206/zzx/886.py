class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        teams = [0] * (n + 1)
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(person, team):
            if teams[person] == -team: return False
            if teams[person] == team: return True
            teams[person] = team
            for next_person in graph[person]:
                if not dfs(next_person, -team):
                    return False
            return True

        for i in range(1, n):
            if teams[i] == 0 and not dfs(i, 1):
                return False
        return True

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        teams = [0] * (n + 1)
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(1, n+1):
            if teams[i] == 0:
                teams[i] = 1
                Q = collections.deque([i])
                while Q:
                    p = Q.popleft()
                    for neighbor in graph[p]:
                        if teams[neighbor] == teams[p]: return False
                        elif teams[neighbor] == 0:
                            teams[neighbor] = -teams[p]
                            Q.append(neighbor)
        return True

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        teams = [0] * (n + 1)
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        parent = list(range(n+1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = parent[find(y)]

        for i in range(1, n+1):
            for j in graph[i]:
                if find(i) == find(j): return False
                union(j, graph[i][0])
        return True
