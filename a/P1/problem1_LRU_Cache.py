class Node(object):

    def __init__(self, key, value):
        self.k = key
        self.v = value
        self.pre = None
        self.next = None

    def update(self, key, value):
        self.k = key
        self.v = value

class LRU_Cache(object):

    def __init__(self, capacity):
        # Intialize class variables
        self.capacity = capacity
        self.cache = dict({})
        self.head = self.tail = None

    def get(self, key) -> int:
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.cache.get(key)
        if node == None:
            return -1
        self.remove(node)
        self.addToHead(node)
        return node.v

    def set(self, key, value) -> None:
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        node = None
        if key in self.cache:
            node = self.cache.get(key)
            node.v = value
            self.remove(node)
        elif len(self.cache) < self.capacity:
            node = Node(key, value)
        else:
            node = self.tail
            self.remove(node)
            node.update(key, value)
        self.addToHead(node)

    def remove(self, node) -> Node:
        self.cache.pop(node.k)
        if node.pre != None:
            node.pre.next = node.next
        if node.next != None:
            node.next.pre = node.pre
        
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.pre
        node.pre = node.next = None
        return node

    def addToHead(self, node) -> Node:
        self.cache[node.k] = node
        if self.head == None:
            self.head = self.tail = node
        else:
            # head != null
            node.next = self.head
            self.head.pre = node
            self.head = node
        return node

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))             # returns 1
print(our_cache.get(2))             # returns 2
print(our_cache.get(9))            # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))            # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(None, float('-inf'))
print(our_cache.get(None))  # -inf

# Test Case 2
our_cache.set('', -1000)
print(our_cache.get(''))  # -1000

# Test Case 3
our_cache.set(float('inf'), 2147483647 + 1)
print(our_cache.get(float('inf')))  #2147483648

our_cache.set(pow(2, 32), float('inf'))
print(our_cache.get(pow(2, 32)))   # inf