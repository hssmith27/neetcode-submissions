class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.first, self.last = None, None

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.nodes.keys()) >= self.capacity:
                self.remove(self.last)
            self.insert(Node(key, value))

    def remove(self, node):
        if node.next is None:
            if node.prev is None:
                self.first = None
                self.last = None
            else:
                self.last = node.prev
                node.prev.next = None
                node.prev = None
        else:
            if node.prev is None:
                self.first = node.next
                node.next.prev = None
                node.next = None
            else:
                previous = node.prev
                following = node.next
                node.prev = None
                node.next = None
                previous.next = following
                following.prev = previous
        self.nodes.pop(node.key)

    def insert(self, node):
        if self.first is None:
            self.last = node
        else:
            node.next = self.first
            self.first.prev = node
        self.first = node
        self.nodes[node.key] = node

        
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None