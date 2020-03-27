''''
https://leetcode.com/problems/sliding-window-maximum/

Combile 2 pages to understand this algorithm:
https://leetcode.com/problems/sliding-window-maximum/discuss/384132/easy-peasy-python-O(n)-using-deque(list)-with-explanation

https://www.youtube.com/watch?v=39grPZtywyQ&t=288s

'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #[1,3,-1,-3,5,3,6,7]
        
        dequeue = []
        #stage 1
        for i in range(k):
            while dequeue and dequeue[-1][1] <= nums[i]:
                dequeue.pop()
            dequeue.append((i, nums[i]))
        #stage 2: 
        rst = [dequeue[0][1]]
        for i in range(k, len(nums)):
            #delete  if the first is that idnex
            if(i-k == dequeue[0][0]):
                dequeue.pop(0)
            
            #append and pop the weak point
            while dequeue and dequeue[-1][1] <= nums[i]:
                dequeue.pop()
            
            dequeue.append((i, nums[i]))
            
            # get result 
            rst.append(dequeue[0][1])
        return rst