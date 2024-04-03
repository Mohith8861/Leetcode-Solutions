// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        h = 0
        def height(root, h):
            if(root == None):
                return 0
            if (root.left == None and root.right == None):
                return 1
            else:
                return 1 + max(height(root.left, h), height(root.right, h))
        return height(root, h)