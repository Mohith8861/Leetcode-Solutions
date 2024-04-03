// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if(not root):
            return 0
        count= [0]
        maxi = root.val
        def dfs(root,max):
            res = 0
            if not root:
                return res
            if(root.val >= max):
                max = root.val
                res = 1
            res += dfs(root.left,max) + dfs(root.right,max)
            return res

        return(dfs(root,maxi)) 

            