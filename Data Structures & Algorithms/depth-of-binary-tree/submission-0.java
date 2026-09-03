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
    public int maxDepth(TreeNode root) {
        return maxDepthH(root, 0);
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
