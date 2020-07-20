'''
https://leetcode.com/problems/word-search-ii/
'''
class Node:
    def __init__(self):
        self.child = {}
        self.cnt = 0
        self.ss = ""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        row , col = len(board), len(board[0])
        if row == 0 or col == 0: return []
        
        # buil the tree
        root = Node()
        for word in words:
            node = root
            for c in word:
                if c not in node.child:
                    node.child[c] = Node()
                node = node.child[c]
            node.cnt += 1
            node.ss = word
        rst = []
        
        
        def f(x,y, root):
            
            if x not in range(row) or y not in range(col) : return 
            
            s = board[x][y]                        
            if s not in root.child: return              
            if root.child[s].cnt >= 1:
                rst.append(root.child[s].ss)
                root.child[s].cnt = 0
                
           
            board[x][y] = "*"
            f(x+1, y, root.child[s])
            f(x-1, y, root.child[s])
            f(x, y+1, root.child[s])
            f(x, y-1, root.child[s])
            
            
            board[x][y] = s
            
            
        for r in range(row):
            for c in range(col):
                if board[r][c] in root.child:
                    f( r, c, root )
              
        
        return rst
        