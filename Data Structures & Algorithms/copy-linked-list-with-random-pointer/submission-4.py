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
        randoms = {None : None} # real : fake
        prev = Node(0)
        curr = head

        while curr is not None:
            duplicate = Node(curr.val)
            prev.next = duplicate
            prev = duplicate
            randoms[curr] = duplicate
            curr = curr.next

        curr = head
        while curr is not None:
            randoms[curr].random = randoms[curr.random]
            curr = curr.next

        return randoms[head]

        




