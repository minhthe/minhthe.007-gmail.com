'''
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
'''
class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        u, v  = min(salary), max(salary)
        
        return ( sum(salary) - u - v) / (n -2)