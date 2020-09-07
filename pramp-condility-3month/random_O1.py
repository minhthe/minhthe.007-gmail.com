'''https://leetcode.com/problems/insert-delete-getrandom-o1'''

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.mp = {}
        self.cnt = 0 

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.mp:
            return False
        else:
            self.mp[val] = self.cnt 
            self.arr.append(val)
            self.cnt +=1
            # print(self.arr, self.mp, self.cnt )
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mp:
            
            # 1 2 3 4 5
            idx = self.mp[val]
            
            tmp = self.arr[-1] 
            
            self.arr[idx] = tmp
            
            self.mp[tmp] = idx
            
            del self.mp[val]
            self.arr.pop()
            self.cnt-=1
            
            
            
            
            
            
            
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[ random.randint(0, self.cnt-1) ]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()