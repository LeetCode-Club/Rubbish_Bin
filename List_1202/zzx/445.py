# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 对于需要逆序的listnode
# 首先考虑用栈存储listnoded的value 然后进行计算
#curnode=ListNode(cur) curnode.next=res res=curnode 逆向新建链表
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1=[]
        stack2=[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next
        while l2:
            stack2.append(l2.val)
            l2=l2.next
        carry=0
        res=None
        while stack1 or stack2 or carry!=0:
            a=stack1.pop()if stack1 else 0
            b=stack2.pop() if stack2 else 0
            cur=a+b+carry
            carry=cur//10
            cur=cur%10
            curnode=ListNode(cur)
            curnode.next=res
            res=curnode
        return res
        
        