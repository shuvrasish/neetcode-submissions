# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        prev = None
        p = second

        while p:
            nextnode = p.next
            p.next = prev
            prev = p
            p = nextnode

        first, second = head, prev

        while first and second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first = next1
            second = next2



        

        