

class Node: 
    def __init__(self, value = 0):
        
        self.prev = self.next = None
        self.value = value
        
class DoublyLinkedList:
    def __init__(self):
        self.head= Node()
        self.tail = Node()
        self.head.next= self.tail 
        self.tail.prev = self.head
    
    
    def append(self, value):
        node = Node(value = value)
        prev = self.tail.prev
        self.tail.prev = node 
        node.next = self.tail
        node.prev = prev
        prev.next= node
        
    def erase(self, node):
        prev = node.prev
        next = node.next 
        prev.next = next 
        next.prev = prev 
    
    def end(self):
        return self.tail
    def begin(self):
        return self.head.next 
capacity = 0 
dll = DoublyLinkedList()
cache= {}
 
def get(key):
    if key in cache:
        dll.erase(cache[key][1])
        dll.append(key)
        cache[key][1] = dll.end().prev
        return cache[key][0]
        
    return 'NULL'
    
def set(key, value):
    if key not in cache and len(cache) == capacity:
        cache.pop(dll.begin().value)
        dll.erase(dll.begin())
        
    elif key in cache:
        dll.erase(cache[key][1])
    dll.append(key)
    cache[key] = [value, dll.end().prev]
    




if __name__ == '__main__':
    
    capacity = 3 
    set(1, 'John')
    set(2, 'Usha')
    set(3, 'Summer')
    set(4, 'Bella')
    set(4, 'Bella')
    print(get(2))
    print(get(1))
    
    set(3, "Alice")
    
    print(get(3))
    
    print(get(2))
    
    print(get(5))
    
    set(1, 'John')
    
    set(1, 'John')
    
    