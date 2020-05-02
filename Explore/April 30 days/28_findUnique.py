class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    
    def __init__(self, k):
        
        self.capacity = k
        self.head = self.tail = Node(0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def append(self,val):
        node = Node(val)
        dummy = self.tail.prev 
        node.next = self.tail
        self.tail.prev = node
        dummy.next = node
        node.prev = dummy
        self.capacity += 1
    
    def delete(self, node):
        if(self.capacity):
            np = node.next
            pp = node.prev
            np.prev = pp
            pp.next = np
            self.capacity -= 1
        
        
class FirstUnique:

    def __init__(self, nums: List[int]):
        
        self.dequeue = DLL(0)
        self.mp = {}
        for item in nums:
            if item in self.mp:
                self.dequeue.delete(self.mp[item][0])
                self.mp[item][1] = False
            else:
                self.dequeue.append(item)
                self.mp[item] = [self.dequeue.tail.prev, True]
                
            
        
        
        
    def showFirstUnique(self) -> int:

        if self.dequeue.capacity:
            return self.dequeue.head.next.val
        return -1
    
    def add(self, value: int) -> None:
        if value in self.mp :
            if self.mp[value][1]:
                self.dequeue.delete(self.mp[value][0])
                self.mp[value][1] = False
        else:
            self.dequeue.append(value)
            self.mp[value] = [self.dequeue.tail.prev, True]
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)