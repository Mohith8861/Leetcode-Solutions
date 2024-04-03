// https://leetcode.com/problems/kth-smallest-element-in-a-bst

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        ArrayList<Integer> l = new ArrayList<Integer>();
        inorder(root,k,l);
        return (l.get(k-1));
    }
    private void inorder(TreeNode node, int k, ArrayList<Integer> l ){
        if(node == null)
            return ;
        inorder(node.left,k,l);
        l.add(node.val);
        inorder(node.right,k,l);
        if(l.size() >= k)
            return;
    }
        
}