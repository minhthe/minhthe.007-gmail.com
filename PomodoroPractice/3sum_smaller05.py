'''
https://www.lintcode.com/problem/3sum-smaller/
'''
class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        rst = 0 
        nums.sort()
        n = len(nums)
    
        for i in range(0, n - 2):
            k = i + 1 
            j = n - 1
            while k < j:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    rst += (j - k)
                    k += 1
                else: 
                    j -= 1 
        return rst
                