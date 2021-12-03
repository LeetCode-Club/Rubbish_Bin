class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        c = s = f = head # 初始化快慢指针的起点和相遇点
        while f and f.next: # 快指针循环条件
            s,f = s.next,f.next.next # 快慢指针同时右移动
            if s == f: # 相遇点
                while c != s: # 寻找入环点
                    c,s = c.next,s.next # 同时移动直到相遇
                return c # 返回入环点
        return None # 未相遇，返回空

