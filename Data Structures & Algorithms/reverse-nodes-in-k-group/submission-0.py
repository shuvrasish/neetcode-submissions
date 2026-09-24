# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, l: Optional[ListNode]) -> Optional[ListNode]:
        p, prev = l, None

        while p:
            next = p.next
            p.next = prev
            prev = p
            p = next
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head

        cnt = 0
        lastEnd = ListNode()
        lastEnd.next = head
        currHead = None
        while p:
            cnt += 1
            if cnt == k:
                cnt = 0 #reset the count

                currStart = lastEnd.next #get current start for reversal
                currNextHead = p.next # get next head to link reversed link to

                p.next = None # set current tail to point to null so that only this part gets reversed

                reversedList = self.reverseList(currStart)
                if not currHead:
                    currHead = reversedList

                lastEnd.next = reversedList #link last tail to current reversed head
                currStart.next = currNextHead #link current tail to next head
                lastEnd = currStart #set new lastend

                p = currNextHead
            else:
                p = p.next
    
        return currHead if currHead else head

