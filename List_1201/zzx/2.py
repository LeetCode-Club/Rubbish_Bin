#顺序遍历较为简单 新建listnode的方法如*
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newhead=ListNode(0)
        newpoint=newhead
        p1,p2=l1,l2
        while p1 or p2:
            a=p1.val if p1 else 0
            b=p2.val if p2 else 0
            result=(a+b+newpoint.val)%10
            flag=(a+b+newpoint.val)//10
            if p1:
                p1=p1.next
            if p2:
                p2=p2.next
            newpoint.val=result
            if p1 or p2 or flag>0:
                newpoint.next=ListNode(flag)#*
                newpoint=newpoint.next
        return newhead