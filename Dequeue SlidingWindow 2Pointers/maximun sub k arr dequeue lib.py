import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.de = collections.deque([])
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if(key in self.cache): 
            self.de.remove(key)
            self.de.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if(key not in self.cache and self.capacity >0):
            self.capacity -= 1
           
        elif(key in self.cache):
            self.de.remove(key)
        else: 
            tmp = self.de.popleft()
            self.cache.pop(tmp)
        self.cache[key] = value
        self.de.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

