// https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reveerse(root):
            if root == None:
                return root
            if (root.left == None and root.right == None):
                return root
            root.left, root.right = root.right, root.left
            reveerse(root.left)
            reveerse(root.right)
        reveerse(root)
        return root
