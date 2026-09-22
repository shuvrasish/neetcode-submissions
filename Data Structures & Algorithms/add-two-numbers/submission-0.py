class Solution:

    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        
        p1, p2 = l1, l2
        res = ListNode(-1)

        p = res
        carry = 0

        while p1 or p2 or carry:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0

            z = x + y + carry

            if z > 9:
                carry = z // 10
                z %= 10
            else:
                carry = 0

            node = ListNode(z)
            p.next = node
            p = node

            if p1:
                p1 = p1.next

            if p2:
                p2 = p2.next
        
        return res.next