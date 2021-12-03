# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#最基本的listnode变换 首先新建dummyhead 令dummyhead.next指向head
#新建temp 
#对于基本变换步骤 将node2给到temp的next 然后原本node2的next成为node1的next 然后node2的next指向node1 最后将temp改成node1 进行下一个操作
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead=ListNode(0)
        dummyhead.next=head
        temp=dummyhead
        while temp.next and temp.next.next:
            node1=temp.next
            node2=temp.next.next
            temp.next=node2
            node1.next=node2.next
            node2.next=node1
            temp=node1
        return dummyhead.next


    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

#递归做法
            
        