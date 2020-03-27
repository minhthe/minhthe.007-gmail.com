'''
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rst = int(1e9)
        def f(nums, rst, pos):
            tmp = -int(1e9)
            last_pos = -1
            for i in range(0, len(nums)):
                
                if nums[i] >= tmp and nums[i] <= rst and i not in pos :
                    tmp = nums[i]
                    last_pos = i
            pos[last_pos] = True
            return tmp, pos
        pos = {}      
        for i in range(k):
            rst, pos = f(nums, rst, pos)
        return rst