# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        last1 = None
        while fast and fast.next:
            last1 = slow
            slow = slow.next
            fast = fast.next.next
        
        if last1:
            last1.next = None
        
        prev = None
        p = slow

        while p:
            nextnode = p.next
            p.next = prev
            prev = p
            p = nextnode


        p1, p2 = head, prev
        last = None

        while p1 and p2:
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p2.next = next1

            p1 = next1
            last = p2
            p2 = next2

        if p2:
            last.next = p2



        

        