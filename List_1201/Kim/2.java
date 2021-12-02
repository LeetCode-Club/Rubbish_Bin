/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode res = dummy;
        if (l1 == null && l2 == null)
            return null;
        if (l1 == null || l2 == null)
            return l1 == null ? l2 : l1;
        int curSum = 0;
        while (l1 != null || l2 != null || curSum != 0) {
            if (l1 != null) {
                curSum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                curSum += l2.val;
                l2 = l2.next;
            }
            // judge curSum % 10
            dummy.next = new ListNode(curSum % 10);
            curSum /= 10;
            dummy = dummy.next;
        }
        return res.next;
    }
}