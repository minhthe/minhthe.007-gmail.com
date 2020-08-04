class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1: return True
        if num ==0 or num & 1: return False
        else: 
            if num % 4 == 0:
                return self.isPowerOfFour(num//4)
            return False
            
        
        