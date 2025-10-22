import collections
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    """
    Performs a deep copy of a graph using Breadth-First Search (BFS).
    Time Complexity: O(V + E) | Space Complexity: O(V)
    """
    if not node:
        return None

    # Hash Map: Stores the mapping from Original Node -> Cloned Node
    # Key concept: Allows O(1) check if a node has been cloned yet.
    old_to_new = {} 
    
    # 1. Start BFS with the given node
    # Clone the starting node immediately
    new_root = Node(node.val)
    old_to_new[node] = new_root
    
    # Queue for BFS traversal (stores original nodes to visit)
    queue = collections.deque([node]) 

    while queue:
        # Get the original node to process
        original_node = queue.popleft()
        
        # Get its corresponding clone from the Hash Map
        cloned_node = old_to_new[original_node]
        
        # 2. Iterate through all neighbors of the original node
        for neighbor in original_node.neighbors:
            
            # Check if the neighbor has already been cloned (O(1) Hash Map lookup)
            if neighbor not in old_to_new:
                
                # If NOT cloned: 
                # a) Create the clone
                new_neighbor = Node(neighbor.val)
                
                # b) Store the mapping in the Hash Map
                old_to_new[neighbor] = new_neighbor
                
                # c) Add the original neighbor to the queue for traversal
                queue.append(neighbor)
            
            # 3. Connect the edges: Get the neighbor's clone and add it
            cloned_neighbor = old_to_new[neighbor]
            cloned_node.neighbors.append(cloned_neighbor)
            
    return new_root

# ----------------------------------------------------------------------
# --- Setup and Test Case ---
# Graph structure: 1 -- 2, 2 -- 3, 3 -- 4, 4 -- 1
# ----------------------------------------------------------------------

# Helper function to build the sample graph
def build_sample_graph():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    
    node1.neighbors.extend([node2, node4])
    node2.neighbors.extend([node1, node3])
    node3.neighbors.extend([node2, node4])
    node4.neighbors.extend([node1, node3])
    
    return node1 # Start from node 1

# Helper function to verify the clone (simple check)
def verify_clone(original_start, clone_start):
    if not original_start and not clone_start: return True
    if not original_start or not clone_start: return False
    
    # BFS to check nodes and values
    q_orig = collections.deque([original_start])
    q_clone = collections.deque([clone_start])
    visited_orig = {original_start}
    visited_clone = {clone_start}
    
    while q_orig:
        o = q_orig.popleft()
        c = q_clone.popleft()
        
        if o.val != c.val or len(o.neighbors) != len(c.neighbors):
            return False # Value or degree mismatch
        
        for o_n, c_n in zip(o.neighbors, c.neighbors):
            if o_n.val != c_n.val: 
                return False # Neighbor value mismatch
            
            if o_n not in visited_orig:
                visited_orig.add(o_n)
                visited_clone.add(c_n)
                q_orig.append(o_n)
                q_clone.append(c_n)
    return True and len(visited_orig) == len(visited_clone)


if __name__ == '__main__':
    original_graph = build_sample_graph()
    cloned_graph = cloneGraph(original_graph)
    
    print("--- Graph Traversal & Cloning (BFS) ---")
    print("Original Graph Node 1 Value:", original_graph.val)
    print("Cloned Graph Node 1 Value:", cloned_graph.val)
    
    # Verify that they are different objects (deep copy)
    print("Are they the same object in memory? (Should be False):", original_graph is cloned_graph)
    
    # Verify the structure is the same
    is_valid_clone = verify_clone(original_graph, cloned_graph)
    print("Is the cloned structure correct? (Should be True):", is_valid_clone)
    
    # Check neighbors of original node 1
    orig_neighbors = [n.val for n in original_graph.neighbors]
    clone_neighbors = [n.val for n in cloned_graph.neighbors]
    print(f"Original Node 1 Neighbors: {orig_neighbors}")

    print(f"Cloned Node 1 Neighbors: {clone_neighbors}")
