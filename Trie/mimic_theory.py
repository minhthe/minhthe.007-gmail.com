

#step 1: defined node
class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()

#step 2: addword in the root
def addWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            tmp.child[ch] = Node()
        tmp  = tmp.child[ch]
    tmp.countWord += 1


#step 3: find the word in the tree:
def findWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return False
        tmp = tmp.child[ch]
    return tmp.countWord > 0

#step 4: remove the word :

#4a:
def isWord(node):
    return node.countWord != 0

#4b
def isEmpty(node):
    return len(node.child) == 0

#4c    
def removeWord(root, s, level, _len):
    if root == None:
        return False
    if level == _len:
        if root.countWord > 0:
            root.countWord -= 1 
            return True 
        return False 
    
    ch = s[level]
    
    flag = removeWord(root.child[ch], s, level + 1, _len)
    
    if flag == True and isWord(root.child[ch]) == False and isEmpty(root.child[ch]) == True:
        
        del root.child[ch]
        
        root.child[ch] = None
        
    return flag

if __name__ == '__main__':
    
    #step 1
    root = Node()
    
    #step 2
    addWord(root, 'the')
    addWord(root, 'then')
    addWord(root, 'bigo') 
    
    #step 3
    print(findWord(root, 'there')) 
    print(findWord(root, 'th'))
    print(findWord(root, 'the'))
    
    #step 4
    removeWord(root, 'bigo', 0, 4)
    removeWord(root, 'the', 0, 3)
    removeWord(root, 'then', 0, 4)