# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head):
            curr = head
            prev = None
            
            while curr is not None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            return prev

        newHead = reverseList(head)
        curr = newHead

        i = 1
        prev = None
        while i != n:
            prev = curr
            curr = curr.next
            i += 1

        if prev is not None:
            prev.next = curr.next
        else:
            newHead = newHead.next

        res = reverseList(newHead)
        return res

