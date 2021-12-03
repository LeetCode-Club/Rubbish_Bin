class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        dire=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=[[0]*n for i in range(m)]
        def dfs(i,j,key):
            image[i][j]=newColor
            visited[i][j]=1
            for xx,yy in dire:
                if 0<=i+xx<m and 0<=j+yy<n and image[i+xx][j+yy]==key and visited[i+xx][j+yy]==0:
                    dfs(i+xx,j+yy,key)
        visited[sr][sc]=1
        dfs(sr,sc,image[sr][sc])
        return image