// https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        h = 0
        def height(root):
            if(root == None):
                return 0
            if (root.left == None and root.right == None):
                return 1
            if (root.left == None):
                return 1 + height(root.right)
            if (root.right == None):
                return 1 + height(root.left)
            else:
                return 1 + min(height(root.left), height(root.right))
        return height(root)