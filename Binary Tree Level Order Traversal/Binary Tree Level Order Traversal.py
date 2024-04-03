// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        if(not root):
            return []
        q.append(root)
        R = []
        while(q):
            a = []
            for i in range(len(q)):
                x = q.pop(0)
                a.append(x.val)
                if(x.left):
                    q.append(x.left)
                if(x.right):
                    q.append(x.right)
            R.append(a)
        return R