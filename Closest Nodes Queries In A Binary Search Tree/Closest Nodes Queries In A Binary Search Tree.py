// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        A = []
        R = []
        def inorder(root):
            if not root :
                return
            inorder(root.left)
            A.append(root.val)
            inorder(root.right)
        inorder(root)
        def search(A, l, h, k):
            if l > h:
                return [l,h]
            mid = (l + h) // 2
            if A[mid] == k:
                return [mid]
            if A[mid] > k:
                return search(A, l, mid - 1, k)
            else:
                return search(A, mid + 1, h, k)
        for i in queries:
            x = search(A, 0, len(A) - 1, i)
            if len(x) == 2:
                if x[0] == 0:
                    R.append([-1, A[x[1] + 1]])
                elif x[0] == len(A):
                    R.append([A[x[0] - 1], -1])
                else:
                    R.append([A[x[0] - 1], A[x[1] + 1]])
            else:
                R.append([A[x[0]], A[x[0]]])
        return R