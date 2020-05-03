class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        rst = 0
        n = len(nums)
        for i in range(n):
            u = nums[i]
            v = nums[i]
            for j in  range(i+1, n+1):
                # print(nums[j-1])
                u = min(u, nums[j-1])
                v = max(v, nums[j-1])
                if( abs(u -v) > limit):
                    break
                rst = max(rst, j - i )
                # print(nums[i:j])
        
        return rst 