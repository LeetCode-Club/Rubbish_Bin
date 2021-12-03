/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

 //the difference between this and #141 is that in this q we should find the intersection node
 //the solution given below can be proved with math method.
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;       
            if(fast == slow){
                ListNode ptr = head;
                while(ptr != slow){
                    slow = slow.next;
                    ptr = ptr.next;
                }
                return ptr;
            }
        }
        return null;
    }
}