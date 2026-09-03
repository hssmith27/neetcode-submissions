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
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        }
        if (maxDepthH(root.left, 0) - maxDepthH(root.right, 0) == 1 || 
        maxDepthH(root.left, 0) - maxDepthH(root.right, 0) == 0 || maxDepthH(root.left, 0) - maxDepthH(root.right, 0) == -1) {
            return true && isBalanced(root.left) && isBalanced(root.right);
        }
        else {
            return false;
        }
    }

    public int maxDepthH(TreeNode current, int depth) {
        if (current == null) {
            return depth;
        }
        else {
            return Math.max(maxDepthH(current.left, depth + 1), maxDepthH(current.right, depth + 1));
        }
    }
}
