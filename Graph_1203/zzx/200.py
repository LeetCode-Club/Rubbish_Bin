class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        m=len(grid)
        n=len(grid[0])
        def dfs(i,j):
            grid[i][j]="0"
            for xx,yy in directions:
                if 0<=i+xx<m and 0<=j+yy<n and grid[i+xx][j+yy]=="1":
                    dfs(i+xx,j+yy)
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    res+=1
        return res
                    
            
        
        