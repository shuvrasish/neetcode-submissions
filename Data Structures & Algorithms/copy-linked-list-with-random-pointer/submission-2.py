"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        oldToCopy = {}

        p = head
        while p:
            copy = Node(p.val)
            oldToCopy[p] = copy
            p = p.next
        
        p = head
        while p:
            copy = oldToCopy[p]
            copy.next = oldToCopy[p.next] if p.next else None
            copy.random = oldToCopy[p.random] if p.random else None
            p = p.next
        
        return oldToCopy[head]



        