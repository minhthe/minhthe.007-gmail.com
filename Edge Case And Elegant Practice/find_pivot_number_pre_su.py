'''https://leetcode.com/problems/find-pivot-index'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx = -1 
        if len(nums) == 0: return -1 
        prefix_sum = [0 for i in range(len(nums))]
        sufix_sum = [0 for i in range(len(nums))]
        
        
        prefix_sum[0] = nums[0]
        sufix_sum[len(nums) -1] =  nums[len(nums) -1]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]  
        for i in range(len(nums) - 2, -1, -1):
            sufix_sum[i] = sufix_sum[i + 1] + nums[i]
        prefix_sum = [0] + prefix_sum  + [0] 
        sufix_sum = [0] +sufix_sum  + [0]
        
        
        for i in range(1, len(nums)+1):
            if prefix_sum[i-1] == sufix_sum[i+1]:
                return i - 1
        return idx
    
        
'''
[-1,-1,0,1,1,0]
-------------- 0

[0, -1 ,1 ]

0 0 - 1 0 0
0 0  0 1 0
[1,7,3,6,5,6]
 1 8 11    
         11 6
[0 , 0]

[0, -1 ,1 ]

[0]

cover the edge -> need apeend left and right wiht 0 value 


step 1: prefix the sum
step 2: sufix the sum 
step 3 : add 0 to head and tail of list and checking that the postiong that sum left side 
right side equally 
'''        