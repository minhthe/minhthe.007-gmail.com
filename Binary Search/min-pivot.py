
'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/604156/Python-Practicing-Intuition-way-O(n)-and-BS-way-O(log(n))

'''class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        n = len(nums)
        
        if n == 1: return nums[0]

        l , r = 0, n - 1
        
        if nums[l] < nums[r]: return nums[l]
        
        while(l <= r):
            mid = int( (r-l)/2 + l )
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid -1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[l]:
                l = mid + 1
            else: 
                r = mid - 1    