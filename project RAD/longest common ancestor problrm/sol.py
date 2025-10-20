from typing import Optional

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
def lowestCommonAncestor(root:TreeNode,p:TreeNode,q:TreeNode)-> TreeNode:
    if not root:
        return None
    if root==p or root==q:
        return root
    left_lca=lowestCommonAncestor(root.left,p,q)
    right_lca=lowestCommonAncestor(root.right,p,q)
    
    if left_lca and right_lca:
        return root
    elif left_lca:
        return left_lca
    elif right_lca:
        return right_lca
    else:
        return None

if __name__ == "__main__":
    # Tree Structure for Example: [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    
    # Level 0
    node3 = TreeNode(3)
    
    # Level 1
    node5 = TreeNode(5)
    node1 = TreeNode(1)
    node3.left = node5
    node3.right = node1
    
    # Level 2
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node5.left = node6
    node5.right = node2
    node1.left = node0
    node1.right = node8
    
    # Level 3
    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node2.left = node7
    node2.right = node4
    
    # --- Test 1: p=5, q=1. Expected LCA: 3 ---
    p1, q1 = node5, node1
    lca_node_1 = lowestCommonAncestor(node3, p1, q1)
    print(f"LCA of {p1.val} and {q1.val}: {lca_node_1.val} (Expected: 3)")
    
    # --- Test 2: p=7, q=4. Expected LCA: 2 ---
    p2, q2 = node7, node4
    lca_node_2 = lowestCommonAncestor(node3, p2, q2)
    print(f"LCA of {p2.val} and {q2.val}: {lca_node_2.val} (Expected: 2)")
    
    # --- Test 3: p=6, q=5. Expected LCA: 5 ---
    p3, q3 = node6, node5
    lca_node_3 = lowestCommonAncestor(node3, p3, q3)
    print(f"LCA of {p3.val} and {q3.val}: {lca_node_3.val} (Expected: 5)")