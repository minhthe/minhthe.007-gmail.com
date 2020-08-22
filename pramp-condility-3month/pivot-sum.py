'''
https://leetcode.com/problems/find-pivot-index/
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx = -1
        n = len(nums)
        left, right = [0]*(n+2),[0]*(n+2) 
        for i,item in enumerate(nums):
            left[i+1] = left[i] + item
        for i in range(n-1, -1, - 1):
            # # print('df', nums[i], right[i+1], nums[i]+ right[i+1])
            right[i+1] = right[i+2] + nums[i]
        # print(left, right)
        for i in range(1,n+1,1):
            if left[i-1] == right[i+1]:
                return i - 1 
        
        return idx