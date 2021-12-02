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

 //the difference between this q and #2 is that in this question we should each digit from end to start
 //so we use 2 stacks to store the element in each list so that we can read from end to start, the other thoughts
 //is as same as #2
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Deque<Integer> stk1 = new LinkedList<>();
        Deque<Integer> stk2 = new LinkedList<>();
        while(l1 != null) {
            stk1.push(l1.val);
            l1 = l1.next;
        }
        while(l2 != null) {
            stk2.push(l2.val);
            l2 = l2.next;
        }
        int sum = 0;
        ListNode ans = null;
        while(!stk1.isEmpty() || !stk2.isEmpty() || sum != 0) {
            int a = stk1.isEmpty() ? 0 : stk1.pop();
            int b = stk2.isEmpty() ? 0 : stk2.pop();
            sum += a + b;
            ListNode cur = new ListNode(sum % 10);
            cur.next = ans;
            ans = cur;
            sum /= 10;
        }
        return ans;
    }
}