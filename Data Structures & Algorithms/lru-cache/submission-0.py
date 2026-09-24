from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int
    prev: Optional[Node] = None
    next: Optional[Node] = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(int)

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node: Optional[Node]):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node: Optional[Node]):
        iprev = self.right.prev
        inext = self.right
        iprev.next = node
        node.prev = iprev
        node.next = inext
        inext.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
