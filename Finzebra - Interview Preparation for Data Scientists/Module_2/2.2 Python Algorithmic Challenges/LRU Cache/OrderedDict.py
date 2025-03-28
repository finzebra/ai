from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()  # Use OrderedDict to maintain insertion order
        self.capacity = capacity  # Maximum capacity of the cache

    def get(self, key):
        if key not in self.cache:
            return -1  # Return -1 if the key is not in the cache
        else:
            self.cache.move_to_end(key)  # Move the accessed key to the end
            return self.cache[key]  # Return the value

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)  # Move the existing key to the end
        self.cache[key] = value  # Insert the new key-value pair
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove the least recently used item

# Example usage
lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # Output: 1
lru_cache.put(3, 3)
print(lru_cache.get(2))  # Output: -1 (key 2 was evicted)