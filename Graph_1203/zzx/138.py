"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hashmap = dict()
        dummy = Node(-1)
        tail, tmp = dummy, head
        while tmp:
            node = Node(tmp.val)
            hashmap[tmp] = node
            tail.next = node
            tail = tail.next
            tmp = tmp.next
        tail = dummy.next
        while head:
            if head.random:
                tail.random = hashmap[head.random]
            tail = tail.next
            head = head.next
        return dummy.next
        