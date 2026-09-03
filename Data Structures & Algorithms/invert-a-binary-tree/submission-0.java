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
    public TreeNode invertTree(TreeNode root) {
        invertTreeH(root);
        return root;
    }

    public void invertTreeH(TreeNode current) {
        if (current == null) {
            return;
        }
        TreeNode left = current.left;
        current.left = current.right;
        current.right = left;
        invertTreeH(current.left);
        invertTreeH(current.right);
    }
}
