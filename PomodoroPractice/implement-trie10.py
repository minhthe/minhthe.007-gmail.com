class Node:
    def __init__(self):
        self.child = {}
        self.cnt = 0
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp = self.root
        for c in word:
            if c not in tmp.child:
                tmp.child[c] = Node()
            tmp = tmp.child[c]
        tmp.cnt += 1
               
   # trie = Trie
#insert('abc')  -> 
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp = self.root
        for c in word:
            if c not in tmp.child:
                return False
            tmp = tmp.child[c]
        return tmp.cnt
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp = self.root
        for c in prefix:
            if c not in tmp.child:
                return False
            tmp = tmp.child[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)