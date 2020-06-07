class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        rst = []
        k = n
        a = nums[:k+1]
        b = nums[k:]
        for i in range(n):

            rst.append(a[i])
            rst.append(b[i])
        return rst
        