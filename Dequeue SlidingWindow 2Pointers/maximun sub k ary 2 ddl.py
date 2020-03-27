'''

https://leetcode.com/problems/sliding-window-maximum/


'''
class Node:
    def __init__(self, val):
        self.val = val 
        self.next  = None
        self.prev = None
class DLL:
    
    def __init__(self,k):
        self.capacity = k 
        self.head = self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def append(self, val)    :
        if self.capacity:
            node  = Node(val)
            dummy = self.tail.prev 
            node.next = self.tail
            self.tail.prev = node 
            dummy.next = node
            node.prev = dummy
            self.capacity -= 1 
            return True
        return False
    
    def erase(self, node):
        np = node.next
        pp = node.prev
        np.prev= pp
        pp.next = np
        self.capacity +=1
    
    
    def notEmpty(self, k):
        return self.capacity < k
        
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # 2 stagegs
        #stage 1
        dequeue = DLL(k)
        mp = {}
        
        for i in range(k):
            while(dequeue.notEmpty(k) and dequeue.tail.prev.val <= nums[i] ):
                dequeue.erase(dequeue.tail.prev)
            dequeue.append(nums[i])
            mp[i] = [nums[i], dequeue.tail.prev]
            
        rst = [dequeue.head.next.val]
        for i in range(k ,len(nums)):
            
            if(dequeue.head.next == mp[ i - k ][1]):
                dequeue.erase(dequeue.head.next)
            
            while(dequeue.notEmpty(k) and dequeue.tail.prev.val <= nums[i] ):
                dequeue.erase(dequeue.tail.prev)
            dequeue.append(nums[i])
            mp[i] = [nums[i], dequeue.tail.prev]
            
            rst.append(dequeue.head.next.val)
        return rst