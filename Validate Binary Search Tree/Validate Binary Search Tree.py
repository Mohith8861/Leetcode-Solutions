// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inorder(root,ans):
            if not root:
                return None
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        inorder(root,ans)
        return ans == sorted(ans) and len(ans) == len(set(ans))