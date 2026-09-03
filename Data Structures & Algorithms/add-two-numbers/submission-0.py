# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        current = dummy
        carry = 0

        while (l1 or l2) or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            carry = 0
            if total > 9:
                carry = 1
                total = total % 10

            current.next = ListNode(total, None)
            current = current.next
            
            
            
        return dummy.next