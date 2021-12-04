class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        int[] res = new int[numCourses];
        for(int[] pre : prerequisites) {
            indegree[pre[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        
        for(int i = 0; i < numCourses; i++) {
            if(indegree[i] == 0) queue.offer(i);
        }
        
        int index = 0;
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            res[index++] = cur;
            
            for(int[] pre : prerequisites) {
                if(pre[1] == cur) {
                    indegree[pre[0]]--;
                    if(indegree[pre[0]] == 0) queue.offer(pre[0]);
                }
            }
        }
        
        return index == numCourses ? res : new int[0];
    }
}