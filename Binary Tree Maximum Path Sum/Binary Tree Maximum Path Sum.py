// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        S = [root.val]
        if(not root.left and not root.right):
            return root.val
        def dfs(root):
            if( not root):
                return 0
            l,r = dfs(root.left),dfs(root.right)
            l, r = max(l,0),max(r,0)
            S[0] = max(S[0],root.val + l + r)
            return root.val + max(l , r)
        dfs(root)
        return S[0]

