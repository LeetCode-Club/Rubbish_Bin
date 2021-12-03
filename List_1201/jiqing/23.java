/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<ListNode>((a, b) -> a.val - b.val);
        for(ListNode node : lists) {
            if(node != null) pq.offer(node);
        }
        ListNode ans = new ListNode(0);
        ListNode tail = ans;
        while(!pq.isEmpty()) {
            ListNode cur = pq.poll();
            tail.next = cur;
            tail = tail.next;
            if(cur.next != null) pq.offer(cur.next);
        }
        return ans.next;
    }
}