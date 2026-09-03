# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next, prev = None, None

        # Reverse the second half
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head2 = prev

        while head2 is not None:
            nxtHead, nxtHead2 = head.next, head2.next
            head.next = head2
            head.next.next = nxtHead
            head = nxtHead
            head2 = nxtHead2
            



