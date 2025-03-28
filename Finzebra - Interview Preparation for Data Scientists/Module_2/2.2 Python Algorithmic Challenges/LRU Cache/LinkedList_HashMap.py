class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove a node from the linked list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        # Add a node to the end of the linked list
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Remove the node from its current position
            self._add(node)  # Add it to the end (most recently used)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])  # Remove the existing node
        node = Node(key, value)
        self._add(node)  # Add the new node to the end
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove the least recently used node (head.next)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Example usage
lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # Output: 1
lru_cache.put(3, 3)
print(lru_cache.get(2))  # Output: -1 (key 2 was evicted)