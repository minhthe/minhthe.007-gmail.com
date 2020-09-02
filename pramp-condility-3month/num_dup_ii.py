'''https://leetcode.com/problems/contains-duplicate-ii'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        # run the k first
        if len(nums)<=1 : return False
        for i in range(min(k+1, len(nums))):
            if nums[i] in mp:
                return True
            else:
                mp[nums[i]] = 1
        pos = k + 1
        while pos < len(nums):
            first = pos - k -1 
            mp[nums[first]] -= 1 
            # print(mp)
            if nums[pos] in mp and mp[nums[pos]] >= 1:
                # print(pos)
                return True
            mp[nums[pos]] = 1 
            pos += 1
        # for item in mp:
        #     if mp[item] >= 2: return True
        return False