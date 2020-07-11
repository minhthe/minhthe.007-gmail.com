'''
https://leetcode.com/problems/3sum/
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        rst = []
        mp = {}
        for i in range(len(nums) - 2):
            if nums[i] in mp: continue
            mp[nums[i]] = True
            left = i+1
            right = len(nums) - 1
            while left < right:
                if sum([nums[i] , nums[left] , nums[right]]) == 0:
                    rst.append([nums[i] , nums[left] , nums[right]])
                    
                    while left + 1 < len(nums) and nums[left] == nums[left+1]:
                        left += 1
                    while right + 1 < len(nums) and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif  sum([nums[i] , nums[left] , nums[right]]) > 0:
                    right -= 1
                else:
                    left += 1
        return rst