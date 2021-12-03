//single source bfs, with a large complexity(t)
class Solution {
    int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int n;
    int[][] grid;
    public int maxDistance(int[][] grid) {
        n = grid.length;
        this.grid = grid;
        int ans = -1;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 0) {
                    ans = Math.max(ans, findNearestLand(i, j));
                }
            }
        }
        return ans;
    }
    
    public int findNearestLand(int x, int y) {
        boolean[][] vis = new boolean[n][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y, 0});
        vis[x][y] = true;
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            for(int i = 0; i < 4; i++) {
                int newx = cur[0] + directions[i][0];
                int newy = cur[1] + directions[i][1];
                if(newx < 0 || newx >= n || newy < 0 || newy >= n) continue;
                if(!vis[newx][newy]) {
                    vis[newx][newy] = true;
                    if(grid[newx][newy] == 1) return cur[2] + 1;
                    queue.offer(new int[]{newx, newy, cur[2] + 1});
                }
            }
        }
        return -1;
    }
}


//multi source bfs, this one is better
class Solution {
    int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    public int maxDistance(int[][] grid) {
        int n = grid.length;
        int ans = -1;
        Queue<int[]> queue = new LinkedList<>();
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == 1) {
                    queue.offer(new int[]{i, j, 0});
                }
            }
        }
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            for(int i = 0; i < 4; i++) {
                int newx = cur[0] + directions[i][0];
                int newy = cur[1] + directions[i][1];
                if(newx < 0 || newx >= n || newy < 0 || newy >= n || grid[newx][newy] != 0) continue;
                queue.offer(new int[]{newx, newy, cur[2] + 1});
                grid[newx][newy] = cur[2] + 1;
                queue.offer(new int[]{newx, newy, cur[2] + 1});
                ans = Math.max(ans, cur[2] + 1);
            }
        }
        return ans;
    }
}