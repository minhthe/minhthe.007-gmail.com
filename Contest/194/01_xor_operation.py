class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        rst = start
        for i in range(1, n):
            rst ^= start + 2 * i
        return rst
        