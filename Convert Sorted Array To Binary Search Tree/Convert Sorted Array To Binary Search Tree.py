// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if len(nums)> 0:
                    
            m = len(nums) // 2
            mid= nums[m]
            Root = TreeNode(val = mid)
            Root.left = self.sortedArrayToBST(nums[:m])
            Root.right = self.sortedArrayToBST(nums[m+1:])

            return Root
        
        return None
        


