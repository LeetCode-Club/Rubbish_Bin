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
use <font color = red>*recursion*</font>, we only think about the first 2 node, swap them and make the 2nd node link to swap(2nd.next).
### 206.Reverse Linked List
use <font color = red>*recursion*</font>, we only think about the fisrt 2 node swap them and then recurse the other nodes, return the last node in the end.
### 707.Design Linked List
when we insert the node, make sure we find the correct position to add.
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