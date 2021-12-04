class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> fromWhere = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            fromWhere.add(new ArrayList<Integer>());
        }
        int[] indegree = new int[n];
        for(int x = 0; x < n; x++) {
            for(int y : graph[x]) {
                //it means y can be from x
                fromWhere.get(y).add(x);
            }
            //it means how many node x can reach directly
            indegree[x] = graph[x].length;
        }
        
        Queue<Integer> queue = new LinkedList<Integer>();
        for(int i = 0; i < n; i++) {
            if(indegree[i] == 0) queue.offer(i);
        }
        
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            //iterate every node that can reach cur
            for(int x : fromWhere.get(cur)) {
                indegree[x]--;
                if(indegree[x] == 0) queue.offer(x);
            }
        }
        
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i < n; i++) if(indegree[i] == 0) ans.add(i);
        return ans;
    }
}