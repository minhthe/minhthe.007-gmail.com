'''
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence

'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)

        tmp = (arr[1] -arr[0])
        for i in range(1, n-1):
            if tmp != (arr[i+1] - arr[i]):
                return False
        return True
            
        