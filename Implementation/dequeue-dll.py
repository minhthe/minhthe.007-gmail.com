'''
https://leetcode.com/problems/design-circular-deque
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail # the front
        self.tail.prev = self.head # the rear
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if(self.capacity):
            node = Node(value)
            prev_node = self.tail.prev
            self.tail.prev = node
            node.next = self.tail            
            node.prev = prev_node
            prev_node.next = node
            self.capacity -=1
            return True
        return False
 
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if(self.capacity):
            node = Node(value)
            next_node = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = next_node
            next_node.prev = node
            self.capacity -=1
            return True
        return False
        
    def erase(self, node):
        if(self.isEmpty() is False):
            self.capacity +=1
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            return True
        return False
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        return self.erase( self.tail.prev)

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        return self.erase(self.head.next)
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if(self.isEmpty()): return -1
        return self.tail.prev.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if(self.isEmpty()): return -1
        return self.head.next.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if self.head.next.next == None and self.tail.prev.prev == None else False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if self.capacity == 0 else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()