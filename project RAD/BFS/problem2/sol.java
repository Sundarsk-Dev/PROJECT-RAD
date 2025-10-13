// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

public class sol {

    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        if (root == null)
            return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size(); // number of nodes at this level
            List<Integer> currentLevel = new ArrayList<>();

            // Process one level
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);

                // Add children for next level
                if (node.left != null)
                    queue.offer(node.left);
                if (node.right != null)
                    queue.offer(node.right);
            }

            // Add this level to result
            result.add(currentLevel);
        }

        return result;
    }

    public static void main(String[] args) {
        // Tree 1: [3, 9, 20, null, null, 15, 7]
        TreeNode root1 = new TreeNode(3);
        root1.left = new TreeNode(9);
        root1.right = new TreeNode(20);
        root1.right.left = new TreeNode(15);
        root1.right.right = new TreeNode(7);

        // Tree 2: [1, 2, 3, 4, null, null, 5]
        TreeNode root2 = new TreeNode(1);
        root2.left = new TreeNode(2);
        root2.left.left = new TreeNode(4);
        root2.right = new TreeNode(3);
        root2.right.right = new TreeNode(5);

        List<TreeNode> testRoots = Arrays.asList(root1, root2, null, new TreeNode(1));

        for (TreeNode root : testRoots) {
            List<List<Integer>> result = levelOrder(root);
            System.out.println("Traversal: " + result);
        }
    }
}
