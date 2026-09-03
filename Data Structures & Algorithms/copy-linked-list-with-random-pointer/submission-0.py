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
        copy = {}
        current = head
        while current != None:
            copy[current] = Node(current.val)
            current = current.next
        copy[None] = None
        
        current = head
        while current:
            copy[current].next = copy[current.next]
            copy[current].random = copy[current.random]
            current = current.next
        
        return copy[head]