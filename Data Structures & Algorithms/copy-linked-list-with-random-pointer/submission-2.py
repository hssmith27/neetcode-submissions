"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        currentNew = dummy
        currentOld = head
        old_to_copy = {}

        while currentOld:
            currentNew.next = Node(currentOld.val)
            currentNew = currentNew.next
            old_to_copy[currentOld] = currentNew
            currentOld = currentOld.next

        currentNew = dummy.next
        currentOld = head

        while currentOld:
            if currentOld.random:
                currentNew.random = old_to_copy[currentOld.random]
            currentNew = currentNew.next
            currentOld = currentOld.next


        return dummy.next