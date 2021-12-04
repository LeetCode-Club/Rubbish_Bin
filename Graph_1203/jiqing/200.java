class Solution {
    int m, n;
    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int numIslands(char[][] grid) {
        m = grid.length;
        n = grid[0].length;
        int sum = 0;
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1') {
                    dfs(grid, i, j);
                    sum++;
                }
            }
        }
        
        return sum;

    }
    
    private void dfs(char[][] grid, int x, int y) {
        if(x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == '0') return;
        
        grid[x][y] = '0';
        
        for(int i = 0; i < 4; i++) {
            int newx = x + directions[i][0];
            int newy = y + directions[i][1];
            
            dfs(grid, newx, newy);
        }
        return;
    }
}