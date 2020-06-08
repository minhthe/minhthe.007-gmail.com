'''
https://www.lintcode.com/problem/3sum-smaller/description
'''
class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        n = len(nums)
        cnt = 0 
        nums.sort()
        for i in range(2, n):
            left , right = 0, i - 1 
            while(left < right)    :
                if nums[left] + nums[right] + nums[i] < target:
                    cnt += right - left
                    left += 1
                    
                else:
                    
                    right -= 1 
        return cnt
            
        
        