# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second is not None:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        head2 = prev
        curr = ListNode()

        while head is not None:
            headNext = head.next
            head2Next = None
            if head2 is not None:
                head2Next = head2.next

            curr.next = head
            curr.next.next = head2
            curr = curr.next.next

            head = headNext
            head2 = head2Next
