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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode(0);
        ListNode tail = ans;
        int sum = 0;
        while(l1 != null || l2 != null || sum > 0) {
            sum += (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val);
            tail.next = new ListNode(sum % 10);
            tail = tail.next;
            sum /= 10;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;
        }
        return ans.next;
    }
}