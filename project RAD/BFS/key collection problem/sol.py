from collections import deque
from typing import List, Tuple, Set

def shortestPathAllKeys(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    start_r, start_c = 0, 0
    total_keys = 0
    
    # 1. Preprocessing: Find start and count total keys (K)
    for r in range(m):
        for c in range(n):
            cell = grid[r][c]
            if cell == '@':
                start_r, start_c = r, c
            elif 'a' <= cell <= 'f': # Max 6 keys (a-f)
                total_keys += 1
    
    # Target mask: e.g., if K=2, target is '11' (binary) = 3
    target_mask = (1 << total_keys) - 1
    
    # State: (r, c, keys_mask)
    # Queue: (r, c, keys_mask, distance)
    queue: deque[Tuple[int, int, int, int]] = deque([(start_r, start_c, 0, 0)])
    
    # Visited set stores the state to prevent cycles/redundant work
    visited: Set[Tuple[int, int, int]] = {(start_r, start_c, 0)}

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 4. BFS Traversal
    while queue:
        r, c, mask, dist = queue.popleft()
        
        # Goal Check
        if mask == target_mask:
            return dist

        # Explore 4 Neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # 1. Boundary and Wall Check
            if not (0 <= nr < m and 0 <= nc < n and grid[nr][nc] != '#'):
                continue
            
            cell = grid[nr][nc]
            new_mask = mask
            
            # 2. Key Check (Lowercase)
            if 'a' <= cell <= 'f':
                # Map 'a' to 0, 'b' to 1, etc., and update the bitmask
                key_bit = ord(cell) - ord('a')
                new_mask = mask | (1 << key_bit)
            
            # 3. Lock Check (Uppercase)
            elif 'A' <= cell <= 'F':
                # Map 'A' to 0, 'B' to 1, etc.
                lock_bit = ord(cell) - ord('A')
                
                # Check if the corresponding key is NOT held (key_bit not set in mask)
                if not (mask & (1 << lock_bit)):
                    continue # Cannot pass through this lock
            
            # Check if this new state has been visited
            new_state = (nr, nc, new_mask)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((nr, nc, new_mask, dist + 1))
                
    return -1 # No path found

# --- Test Cases ---

if __name__ == "__main__":
    
    test_cases = [
        (["@.a.#", "###.#", "b.A.B"], 8),
        (["@..aA", "..B#.", "....b"], 10),
        (["@Aa"], -1), # Cannot get A without a
        (["@.a..", "#.###", "b.#.B"], -1) # Path blocked
    ]

    print("--- Shortest Path to Get All Keys (BFS + Bitmasking) Test Results ---")
    
    for grid, expected in test_cases:
        result = shortestPathAllKeys(grid)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        # Print the first row of the grid for input context
        print(f"Grid: {grid[0]}... -> Path Length: {result}, Status: {status}")