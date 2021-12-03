class Solution {
    int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int m, n;
    int area;
    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        m = grid.length;
        n = grid[0].length;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    area = 0;
                    dfs(grid, i, j);
                    max = Math.max(max, area);
                }
            }
        }
        return max;
    }
    
    private void dfs(int[][] grid, int x, int y) {
        grid[x][y] = 0;
        area++;
        for(int i = 0; i < 4; i++) {
            int newx = x + directions[i][0];
            int newy = y + directions[i][1];
            if(newx >= 0 && newx < m && newy >= 0 && newy < n && grid[newx][newy] == 1)
                dfs(grid, newx, newy);
        }
    }
}