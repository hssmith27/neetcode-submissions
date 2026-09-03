# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        current = head
        prevNode = None

        while current.next != None:
            nextNode = current.next # 1 | 2
            current.next = prevNode # head.next = None | 
            prevNode = current # prevNode = head | 
            current = nextNode # current = 1 | 
        
        current.next = prevNode
            
        return current