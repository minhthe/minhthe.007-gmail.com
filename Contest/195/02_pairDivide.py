'''
https://leetcode.com/contest/weekly-contest-195/problems/check-if-array-pairs-are-divisible-by-k/
'''
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        s = sum(arr)
        if s%k==0 : return True
        return False