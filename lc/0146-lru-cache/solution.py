class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:


    def __init__(self, capacity: int):
        self.c = capacity
        self.h = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.h:
            return -1
        
        node = self.h[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            old_node = self.h[key]
            self.remove(old_node)
        node = Node(key, value)
        self.h[key] = node
        self.add(node)

        if len(self.h) > self.c:
            to_delete = self.head.next
            self.remove(to_delete)
            del self.h[to_delete.key]
    
    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
