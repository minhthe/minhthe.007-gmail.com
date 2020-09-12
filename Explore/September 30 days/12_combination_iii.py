
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        tmp = []
        nums = [i for i in range(1, 10)]
      
        ans = []
        def generate(tmp, pos):
            
            if len(tmp) == k and sum(tmp) == n:
                ans.append(tmp[:])
            
            for i in range(pos, len(nums)):
                tmp.append(nums[i])
                generate(tmp, i + 1)
                tmp.pop()
            return ans
            
        return list( list(item) for item in set( tuple(item) for item in generate(tmp , 0)  ) )
        
        