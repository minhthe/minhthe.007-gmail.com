'''
https://leetcode.com/problems/3sum
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rst = []
        nums.sort()
        mp = {}
        for i in range(len(nums)-1):
            j = len(nums) - 1
            k = i + 1
            while(k < j):
                s = nums[i] + nums[k] + nums[j]
                if s == 0 :
                    if  (nums[i], nums[k], nums[j]) not in mp:
                        rst.append([nums[i], nums[k], nums[j]])
                        mp[(nums[i], nums[k], nums[j])] = True
                    k += 1 
                    j -= 1
                elif s > 0 :
                    j -= 1
                else:
                    k += 1
        return rst