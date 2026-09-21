# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        size = 0
        while p:
            size += 1
            p = p.next
        
        if size < 2:
            return None
        
        posFromFront = size - n
        if posFromFront == 0:
            return head.next

        p, prev = head, None

        while posFromFront:
            prev = p
            p = p.next
            posFromFront -= 1
        
        prev.next = p.next

        return head

        


