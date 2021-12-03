# 12.01

## List
| Id  | Name                 | Difficulty | Similar Problems |   |   |   |   |   |   | Comments                   |
|-----|----------------------|------------|------------------|---|---|---|---|---|---|----------------------------|
| 2   | Add Two Numbers      | ★★         | 445              |   |   |   |   |   |   | traversal                  |
| 24  | Swap Nodes in Pairs  | ★★         |                  |   |   |   |   |   |   | reverse                    |
| 206 | Reverse Linked List  | ★★         |                  |92 |   |   |   |   |   | reverse                    |
| 141 | Linked List Cycle    | ★★         | 142              |   |   |   |   |   |   | fast/slow                  |
| 23  | Merge k Sorted Lists | ★★★        | 21               |   |   |   |   |   |   | priority_queue / mergesort |
| 147 | Insertion Sort List  | ★★★        |                  |   |   |   |   |   |   | insertion sort             |
| 148 | Sort List            | ★★★★       |                  |   |   |   |   |   |   | merge sort O(1) space      |
| 707 | Design Linked List   | ★★★★       |                  |   |   |   |   |   |   |                            |
| 146 | LRU Cache            | ★★★★       |                  |   |   |   |   |   |   | veeeeery important!!       |

## jiqing
### 24.Swap Nodes in Pairs
Use <font color = red>*recursion*</font>, we can only think about the first 2 node, swap them and make the 2nd node link to swap(2nd.next).
### 206.Reverse Linked List
Use <font color = red>*recursion*</font>, we can only think about the fisrt 2 node swap them and then recurse the other nodes, return the last node in the end.
### 92.Reverse Linked List II
In this question, we can solve such a subquestion at first:<br>
<font color = green>***Reverse first N nodes of a LinkedList***</font><br>
```
public ListNode reverseN(ListNode head, int n) {
    if(n == 1) {
        successor = head.next;
        return head;
    }
    ListNode last = reverseN(head.next, n - 1);
    head.next.next = head;
    head.next = successor;
    return last;
}
```
Then if left = 1, the question is as same as **Reverse first N nodes of a LinkedList**. If not we can use recursion to move the list to make left = 1.<br>
```
public ListNode reverseBetween(ListNode head, int left, int right) {
    if(left == 1) return reverseN(head, right);
    head.next = reverseBetween(head.next, left - 1, right - 1);
    return head;
}
```
### 707.Design Linked List
When we insert the node, make sure we find the correct position to add.
```
public void addAtIndex(int index, int val) {
    // If index is greater than the length, 
    // the node will not be inserted.
    if (index > size) return;

    // [so weird] If index is negative, 
    // the node will be inserted at the head of the list.
    if (index < 0) index = 0;

    ++size;
    // find predecessor of the node to be added
    ListNode pred = head;
    for(int i = 0; i < index; ++i) pred = pred.next;

    // node to be added
    ListNode toAdd = new ListNode(val);
    // insertion itself
    toAdd.next = pred.next;
    pred.next = toAdd;
}
```
## zixin



## kim