# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        head = ListNode(0, None)
        current = head

        while (cur1 and cur2):
            if (cur1.val < cur2.val):
                current.next = cur1
                current = current.next
                cur1 = cur1.next
                current.next = None
            else:
                current.next = cur2
                current = current.next
                cur2 = cur2.next
                current.next = None

        while cur1:
            current.next = cur1
            current = current.next
            cur1 = cur1.next
            current.next = None

        while cur2:
            current.next = cur2
            current = current.next
            cur2 = cur2.next
            current.next = None  

        return head.next