from typing import Optional

# Conceptual Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    """
    Checks if a binary tree is symmetric around its center.
    """
    if not root:
        return True
    
    # Start the mirror check on the left and right children
    return isMirror(root.left, root.right)

def isMirror(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Helper function to check if two subtrees (p and q) are mirrors of each other.
    """
    
    # Base Case 1: Both nodes are null (end of a branch), they are symmetric
    if p is None and q is None:
        return True
        
    # Base Case 2: One node is null, or their values differ. Not symmetric.
    if p is None or q is None or p.val != q.val:
        return False
        
    # Recursive Step: Check the mirror relationship:
    # 1. p's LEFT must mirror q's RIGHT.
    # 2. p's RIGHT must mirror q's LEFT.
    return isMirror(p.left, q.right) and isMirror(p.right, q.left)

# --- Test Cases ---

if __name__ == "__main__":
    
    # Example 1: Symmetric Tree (Expected: True)
    #      1
    #     / \
    #    2   2
    #   / \ / \
    #  3  4 4  3
    root1 = TreeNode(1, 
                     TreeNode(2, TreeNode(3), TreeNode(4)),
                     TreeNode(2, TreeNode(4), TreeNode(3)))
    
    # Example 2: Asymmetric Tree (Expected: False)
    #      1
    #     / \
    #    2   2
    #     \   \
    #      3   3
    root2 = TreeNode(1, 
                     TreeNode(2, None, TreeNode(3)),
                     TreeNode(2, None, TreeNode(3)))

    print("--- Symmetric Tree (Recursive DFS) Test Results ---")
    
    tests = [(root1, True), (root2, False), (None, True)]
    
    for root, expected in tests:
        result = isSymmetric(root)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        print(f"Test -> Result: {result}, Status: {status}")
