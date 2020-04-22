''''
https://leetcode.com/problems/find-peak-element/discuss/591738/python-practicing-binary-search-with-ologn

Time complexity: O(logn)
Space complexity: O(1)
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums = [-2e32] + nums + [-2e32]
        
        l, r = 0, len(nums) -1
        
        while(l<=r):
        
            mid = int( (r-l)/2 + l )
            
            if( nums[mid -1] < nums[mid] > nums[mid + 1] ): # sastify the requirement.
                return mid - 1                              # -1 because added [-2e32] 
            
            if( nums[mid] < nums[mid+1] ):                  # the array nums in this section is increasing 
                l = mid + 1
            
            else:
                r = mid - 1                                 # the array nums in this section is decreasing
        return -1
                
