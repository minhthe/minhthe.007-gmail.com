'''https://leetcode.com/problems/all-elements-in-two-binary-search-trees'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def f(root):
            if root is None:
                return []
            return f(root.left) + [root.val] + f(root.right)
        part1= f(root1)
        part2 = f(root2)
        rst = []
        l1, l2, r1, r2 = 0, 0 , len(part1), len(part2)
        while l1 < r1 and l2 < r2:
            if part1[l1] <= part2[l2]:
                rst.append(part1[l1])
                l1+=1
            else:
                rst.append(part2[l2])
                l2+=1
        while l1 < r1:
            rst.append(part1[l1])
            l1+=1
        while l2 < r2:
            rst.append(part2[l2])
            l2+=1            
        return rst
        