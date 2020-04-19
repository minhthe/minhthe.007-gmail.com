'''
https://leetcode.com/problems/binary-search/

Time Complextiy: O(log(n))
Space Complexity: O(1)

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        while(l<=r):
            mid = int ((r -l)/2 + l)
            
            if(nums[mid] == target): return mid
            if(nums[mid] > target): r = mid - 1
            else: l = mid + 1
            
            
        return -1