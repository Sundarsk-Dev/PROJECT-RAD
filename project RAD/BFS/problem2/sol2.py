from typing import List, Optional
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs Binary Tree Level Order Traversal using BFS and a queue.
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if not root:
        return []

    # Use a deque for efficient pop operations from the left (queue functionality)
    queue = deque([root])
    result = []

    while queue:
        # Get the number of nodes currently on this level
        level_size = len(queue)
        current_level_nodes = []

        # Process exactly 'level_size' nodes to complete the current level
        for _ in range(level_size):
            node = queue.popleft()
            
            # 1. Record the node's value
            current_level_nodes.append(node.val)

            # 2. Enqueue children for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Add the completed level list to the final result
        result.append(current_level_nodes)

    return result

# --- Test Cases ---

if __name__ == "__main__":
    
    # Tree 1: [3, 9, 20, null, null, 15, 7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    # Tree 2: [1, 2, 3, 4, null, null, 5]
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(4))
    root2.right = TreeNode(3, None, TreeNode(5))
    
    test_cases = [
        (root1, [[3], [9, 20], [15, 7]]),
        (root2, [[1], [2, 3], [4, 5]]),
        (None, []),
        (TreeNode(1), [[1]])
    ]

    print("--- Binary Tree Level Order Traversal Test Results ---")
    
    for root, expected in test_cases:
        result = levelOrder(root)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        # Display the structure simply
        if root:
            root_val = root.val
        else:
            root_val = "None"
            
        print(f"Root: {root_val} -> Traversal: {result}, Status: {status}")