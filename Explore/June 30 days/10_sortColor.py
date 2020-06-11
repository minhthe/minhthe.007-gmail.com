class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mp ={}
        for item in nums:
            mp[item] =  mp[item] + 1 if item in mp else  1
        k = 0
        for item in sorted(mp.items(), key = lambda  x: x[0]):
            for i in range(item[1]):
                nums[k] = item[0]
                k+=1 
        return nums
        