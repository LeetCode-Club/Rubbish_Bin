#两种方法 快慢指针（类似于乌龟赛跑）和利用set的迭代法
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=set()
        while head:
            if head in temp:
                return True
            temp.add(head)
            head=head.next
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast=head.next
        slow=head
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True