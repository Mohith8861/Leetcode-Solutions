// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        M = [0]
        def search(root):
            if(root == None):
                return -1
            l = search(root.left)
            r = search(root.right)
            M[0] = max(M[0],l + r + 2)
            return 1 + max(l,r)
        search(root)
        return M[0]