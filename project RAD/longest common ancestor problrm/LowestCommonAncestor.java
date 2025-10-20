class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int x) {
        val = x;
    }
}

public class LowestCommonAncestor {

    public static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // Base Case 1: If tree is empty
        if (root == null)
            return null;

        // Base Case 2: If we found either p or q
        if (root == p || root == q)
            return root;

        // Recursive Search
        TreeNode leftLCA = lowestCommonAncestor(root.left, p, q);
        TreeNode rightLCA = lowestCommonAncestor(root.right, p, q);

        // Case 1: Found p and q in different subtrees
        if (leftLCA != null && rightLCA != null)
            return root;

        // Case 2: Found in left or right subtree only
        return (leftLCA != null) ? leftLCA : rightLCA;
    }

    public static void main(String[] args) {
        // --- Build Tree ---
        TreeNode node3 = new TreeNode(3);
        TreeNode node5 = new TreeNode(5);
        TreeNode node1 = new TreeNode(1);
        TreeNode node6 = new TreeNode(6);
        TreeNode node2 = new TreeNode(2);
        TreeNode node0 = new TreeNode(0);
        TreeNode node8 = new TreeNode(8);
        TreeNode node7 = new TreeNode(7);
        TreeNode node4 = new TreeNode(4);

        node3.left = node5;
        node3.right = node1;
        node5.left = node6;
        node5.right = node2;
        node1.left = node0;
        node1.right = node8;
        node2.left = node7;
        node2.right = node4;

        // --- Test 1: p=5, q=1 (Expected LCA=3) ---
        TreeNode lca1 = lowestCommonAncestor(node3, node5, node1);
        System.out.println("LCA of 5 and 1: " + lca1.val + " (Expected: 3)");

        // --- Test 2: p=7, q=4 (Expected LCA=2) ---
        TreeNode lca2 = lowestCommonAncestor(node3, node7, node4);
        System.out.println("LCA of 7 and 4: " + lca2.val + " (Expected: 2)");

        // --- Test 3: p=6, q=5 (Expected LCA=5) ---
        TreeNode lca3 = lowestCommonAncestor(node3, node6, node5);
        System.out.println("LCA of 6 and 5: " + lca3.val + " (Expected: 5)");
    }
}
