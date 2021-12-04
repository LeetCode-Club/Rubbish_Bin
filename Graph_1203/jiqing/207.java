class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        int[] res = new int[numCourses];
        
        for(int[] pre : prerequisites) {
            indegree[pre[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<Integer>();
        
        for(int i = 0; i < numCourses; i++) {
            if(indegree[i] == 0) queue.offer(i); 
        }
        
        int index = 0;
        while(!queue.isEmpty()) {
            Integer curr = queue.poll();
            res[index++] = curr;
            
            for(int[] pre : prerequisites) {
                if(pre[1] == curr) {
                    indegree[pre[0]]--;
                    if(indegree[pre[0]] == 0) queue.offer(pre[0]);
                }
            }
        }
        
        return index == numCourses;
    }
}