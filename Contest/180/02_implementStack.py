'''
https://leetcode.com/problems/design-a-stack-with-increment-operation/
'''
class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.maxSize = maxSize
        return None

    def push(self, x: int) -> None:
        if(len(self.arr) < self.maxSize):
            self.arr.append(x)
        return None

    def pop(self) -> int:
        if(len(self.arr)):
            tmp = self.arr.pop()
            return tmp
        return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.arr))
        for i in range(k):
            self.arr[i]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)