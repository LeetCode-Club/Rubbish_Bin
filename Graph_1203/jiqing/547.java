class Solution {
    public int findCircleNum(int[][] isConnected) {
        int len = isConnected.length;
        boolean[] visited = new boolean[len];
        int ans = 0;
        
        for(int i = 0; i < len; i++) {
            if(!visited[i]) {
                dfs(isConnected, visited, len, i);
                ans++;
            }
        }
        return ans;
    }
    
    public void dfs(int[][] isConnected, boolean[] visited, int len, int cur) {
        for(int i = 0; i < len; i++) {
            if(!visited[i] && isConnected[i][cur] == 1) {
                visited[i] = true;
                dfs(isConnected, visited, len, i);
            }
        }
    }
}