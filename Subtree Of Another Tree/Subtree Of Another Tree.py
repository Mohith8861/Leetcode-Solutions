// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root1,root2):
            if(not root1 and not root2):
                return True
            if(root1 and root2 and root1.val ==  root2.val):
                return check(root1.left,root2.left) and check(root1.right,root2.right)
            return False
        def inordercheck(root1,root2):
            if(not root2):
                return True
            if(not root1):
                return False
            if(check(root1,root2)):
                return True
            return (inordercheck(root1.left,root2) or inordercheck(root1.right,root2))
        return inordercheck(root,subRoot)
