class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        pos, j = -1, -1
        
        for i in range(len(nums)):
            if(pos == -1 and nums[i] == 1):
                pos = i
                continue
            if(j == -1 and nums[i] == 1):
                j = i
                # print(j, pos)
                if(j - pos - 1)< k:
                    print(j, pos)
                    return False
                pos = j
                j = -1
        # print(j, pos)
        return True
       