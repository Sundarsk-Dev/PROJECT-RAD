# File: NetworkMapper.py

import collections

# --- 1. DSA Component: Node Class ---

class NetworkNode:
    """Represents a device (server, router) in the network graph."""
    def __init__(self, device_id: int):
        self.val = device_id
        self.neighbors = []
        # Additional metadata for real-world context (not used in algorithm, but important)
        self.status = "UP" 
        self.ip_address = f"192.168.1.{device_id}"

    def __repr__(self):
        # Clean representation for printing
        neighbor_ids = [n.val for n in self.neighbors]
        return f"Node({self.val}, Neighbors: {neighbor_ids})"

# --- 2. Core Algorithm: BFS Clone Function ---

def clone_network_snapshot(start_node: NetworkNode) -> NetworkNode | None:
    """
    Performs a deep copy of a connected graph using BFS and a Hash Map.
    This simulates creating an immediate, independent network snapshot.
    Time Complexity: O(V + E) | Space Complexity: O(V)
    """
    if not start_node:
        return None

    # Hash Map: Stores the mapping from Original Node -> Cloned Node (O(1) lookup)
    # This prevents cycles and avoids re-cloning already-visited nodes.
    old_to_new = {start_node: NetworkNode(start_node.val)}
    
    # Queue for BFS traversal (stores original nodes to process)
    queue = collections.deque([start_node]) 

    while queue:
        original_node = queue.popleft()
        cloned_node = old_to_new[original_node]
        
        # Traverse neighbors
        for neighbor in original_node.neighbors:
            
            # Check if the neighbor has already been cloned (Hash Map check)
            if neighbor not in old_to_new:
                
                # If NOT cloned: 
                # a) Create the clone with the same data (deep copy)
                new_neighbor = NetworkNode(neighbor.val)
                new_neighbor.status = neighbor.status
                new_neighbor.ip_address = neighbor.ip_address
                
                # b) Store the mapping in the Hash Map
                old_to_new[neighbor] = new_neighbor
                
                # c) Add the original neighbor to the queue to traverse its neighbors later
                queue.append(neighbor)
            
            # Connect the edges: Get the neighbor's clone and link it
            cloned_neighbor = old_to_new[neighbor]
            cloned_node.neighbors.append(cloned_neighbor)
            
    return old_to_new[start_node] # Return the cloned starting node


# --- 3. Utility and Demonstration Functions ---

def build_sample_network() -> NetworkNode:
    """Creates a sample connected network topology."""
    node_a = NetworkNode(101)  # Router 101
    node_b = NetworkNode(205)  # Server 205
    node_c = NetworkNode(310)  # Workstation 310
    node_d = NetworkNode(400)  # Load Balancer 400
    
    # Connections (Edges): Undirected
    node_a.neighbors.extend([node_b, node_d])
    node_b.neighbors.extend([node_a, node_c])
    node_c.neighbors.extend([node_b, node_d])
    node_d.neighbors.extend([node_a, node_c])
    
    # Change status of one node for testing
    node_c.status = "DOWN"
    
    return node_a # Start mapping from the Router

def print_bfs_traversal(start_node: NetworkNode, title: str):
    """Prints the discovered nodes in BFS order (level-by-level)."""
    if not start_node: return
    
    print(f"\n--- BFS Traversal: {title} ---")
    queue = collections.deque([start_node])
    visited = {start_node}
    
    while queue:
        node = queue.popleft()
        
        neighbor_ids = [n.val for n in node.neighbors]
        print(f"  > Device {node.val} (IP: {node.ip_address}, Status: {node.status})")
        
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# --- 4. Main Execution ---

if __name__ == "__main__":
    
    # Build the Original Network
    original_network_start = build_sample_network()
    
    print("=" * 60)
    print("🌐 RAD Project: Network Topology Mapper (BFS & Hash Map)")
    print("PITCH: Efficient O(V+E) discovery and snapshotting for network analysis.")
    print("=" * 60)
    
    # 1. Traverse and Print Original Network State
    print_bfs_traversal(original_network_start, "ORIGINAL LIVE NETWORK STATE")
    
    # 2. Create the Deep Copy (Snapshot)
    print("\n--- ACTION: Creating Network Snapshot (Deep Copy via BFS) ---")
    cloned_network_start = clone_network_snapshot(original_network_start)
    
    if cloned_network_start:
        print("✅ Snapshot Created Successfully!")
        
        # 3. Modify the original network AFTER the snapshot
        original_network_start.status = "MAINTENANCE"
        original_network_start.val = 999 # Change ID
        original_network_start.neighbors[0].status = "UPGRADE"

        # 4. Traverse and Print Cloned State (Snapshot)
        print_bfs_traversal(cloned_network_start, "CLONED SNAPSHOT STATE (for Simulation)")
        
        # 5. Verification (Show that the clone is independent)
        print("\n--- Verification of Deep Copy ---")
        print(f"Original Start Node ID (Changed): {original_network_start.val}") # Should be 999
        print(f"Cloned Start Node ID (Unchanged): {cloned_network_start.val}") # Should still be 101
        
        print("\nStatus Check:")
        print(f"Original Server 205 Status (UPGRADE): {original_network_start.neighbors[0].status}")
        print(f"Cloned Server 205 Status (Original UP): {cloned_network_start.neighbors[0].status}")
    
    print("=" * 60)