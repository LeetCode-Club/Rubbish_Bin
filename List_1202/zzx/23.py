class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1,l2):
            d = c = ListNode(-1)
            while l1 and l2:
                if l1.val <= l2.val:
                    c.next,l1 = l1,l1.next
                else:
                    c.next,l2 = l2,l2.next
                c = c.next
            c.next = l1 if l1 else l2
            return d.next
            
        ans = None
        for i in lists:
            ans = merge(ans,i)
        return ans

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1,l2):
            d = c = ListNode(-1)
            while l1 and l2:
                if l1.val <= l2.val:
                    c.next,l1 = l1,l1.next
                else:
                    c.next,l2 = l2,l2.next
                c = c.next
            c.next = l1 if l1 else l2
            return d.next
        def h(l,r):
            if l == r:return lists[l]
            m = (l+r)//2
            s1 = h(l,m)
            s2 = h(m+1,r)
            return merge(s1,s2)
        if not lists : return None
        return h(0,len(lists)-1)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq #调用堆
        minHeap = []
        for listi in lists: 
            while listi:
                heapq.heappush(minHeap, listi)
                listi = listi.next
        dummy = ListNode(0) #构造虚节点
        p = dummy
        while minHeap:
            p.next = heapq.heappop(minHeap)#依次弹出最小堆的数据
            p = p.next
        return dummy.next 