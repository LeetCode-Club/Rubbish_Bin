"""
两种去重方法，
染色
visited

-------
如果有可能有新的连接通量， 则需要新的deque 
========
BFS去重
1. before bfs , during init
2. inside the child block
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # que = collections.deque([])
        # visited = set()
        color0 = 0
        color1 = 1
        color2 = 2
        colorlist = [color0] * len(graph)

        for i in range(len(graph)):
          if colorlist[i] == color0 :
            # que.append((i, color1))
            que = collections.deque([i])
            # 1. 去重1 
            colorlist[i]==color2
            while que:
              node = que.popleft()
              color = colorlist[node]
              oppo_color = color2 if color == color1 else color1
              for i in graph[node]:
                if colorlist[i] == color0:
                  que.append(i)
                  colorlist[i]= oppo_color
                elif colorlist[i] == color:
                  return False
                elif colorlist[i] == oppo_color:
                  continue
        return True
      
"""
DFS

难点在于BFS 可以直接return False 剪纸，
但DFS 需要借助辅助变量 valid
- 过程中如果遇到invalid case， set valid to False
- dfs return
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:  
        color0 = 0
        color1 = 1
        color2 = 2
        colorlist = [color0] * len(graph)
        valid= True
        
        def dfs(node):
          nonlocal valid
          
          color = colorlist[node]
          oppo_color = color2 if color == color1 else color1
          for i in graph[node]:
            if colorlist[i] == color:
              valid = False
              return 
            elif colorlist[i] == color0:
              colorlist[i]= oppo_color
              dfs(i)
              if not valid:
                return
          # return 

        #  因为图中可能含有多个连通域，所以我们需要判断是否存在顶点未被访问，若存在则从它开始再进行一轮 dfs 染色
        for i in range(len(graph)):
          if colorlist[i] == color0:
            colorlist[i]=color1
            dfs(i)
            if not valid:
              break

        return valid
        
#         # time O(n^2 alpha(n)), space O(n)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = parent[find(y)]
        # 遍历每个顶点，将当前顶点的所有邻接点进行合并
        for i in range(n):
            for j in graph[i]:
              #  若某个邻接点在合并前，与当前顶点已经在一个集合中了，说明不是二分图，返回 false。
                if find(i) == find(j): return False
                union(graph[i][0], j)
        return True

      
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color0 = 0
        color1 = 1
        color2 = 2
        colorlist = [color0] * len(graph)
        # valid= True

        def dfs(node):
          # nonlocal valid

          color = colorlist[node]
          oppo_color = color2 if color == color1 else color1
          for i in graph[node]:
            if colorlist[i] == color:
              return False
            elif colorlist[i] == color0:
              colorlist[i]= oppo_color
              
              if not dfs(i):
                return False
          return True

        #  因为图中可能含有多个连通域，所以我们需要判断是否存在顶点未被访问，若存在则从它开始再进行一轮 dfs 染色
        for i in range(len(graph)):
          if colorlist[i] == color0:
            colorlist[i]=color1
            if not dfs(i):
              return False
            # if not valid:
            #   break

        return True
      
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:  
        color0 = 0
        color1 = 1
        color2 = 2
        colorlist = [color0] * len(graph)
        valid= True
        for i in range(len(graph)):
          if not valid: return False
          if colorlist[i]==color0:
            que = [i]
            colorlist[i]= 1
            while que:
              v = que.pop(0)
              color_v = colorlist[v]
              color_oppo = 2 if color_v ==1 else 1
              for u in graph[v]:
                if colorlist[u]== 0:
                  colorlist[u]= color_oppo
                  que.append(u)
                elif colorlist[u]== color_oppo: # already visited
                  continue
                elif colorlist[u]== color_v:
                  valid = False
                  break
                  
        return True