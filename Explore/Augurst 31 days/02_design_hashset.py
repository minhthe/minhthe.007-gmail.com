'''
https://leetcode.com/problems/design-hashset/
'''
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [-1 for i in range(1000001)]
            
            #
        

    def add(self, key: int) -> None:
        self.arr[key] = key

    def remove(self, key: int) -> None:
        # if self.arr[key] != False :
        self.arr[key] = -1
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.arr[key]!=-1:return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)