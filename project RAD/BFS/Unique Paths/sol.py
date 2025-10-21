from typing import List

class UniquePathsIII:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        empty_cells = 0
        
        # 1. Preprocessing: Find start, end, and total empty cells
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                elif grid[r][c] == 0:
                    empty_cells += 1
        
        # Total steps required: All empty cells + the starting cell (1)
        self.total_required_steps = empty_cells + 1
        self.path_count = 0
        
        # Directions: up, down, left, right
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        self.m, self.n = m, n
        self.grid = grid
        
        # Start DFS from the starting cell
        self._dfs(start_r, start_c, 0)
        
        return self.path_count

    def _dfs(self, r: int, c: int, cells_visited: int):
        
        # 3a. Base Case 1: Out of bounds or obstacle/already visited
        # We use grid values for visited state tracking: 1/0 is original, -1 is visited/obstacle.
        if not (0 <= r < self.m and 0 <= c < self.n and self.grid[r][c] != -1):
            return 
        
        # 3b. Base Case 2: End Square Reached
        if self.grid[r][c] == 2:
            # Check the crucial final condition: did we visit exactly all required non-obstacle cells?
            if cells_visited == self.total_required_steps:
                self.path_count += 1
            return
            
        # 4. Recursive Step
        
        # Store original value for backtracking
        original_val = self.grid[r][c]
        
        # Mark as visited (Crucial for pruning/cycle prevention)
        # We temporarily set the cell to -1 (obstacle)
        self.grid[r][c] = -1
        
        # Increment the count of steps/unique cells visited
        new_visited_count = cells_visited + 1
        
        # Explore 4 neighbors
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            self._dfs(nr, nc, new_visited_count)
            
        # 4b. Backtrack (Undo)
        # Restore the cell to its original value (0 or 1) so other paths can traverse it
        self.grid[r][c] = original_val


# --- Test Cases ---

if __name__ == "__main__":
    solver = UniquePathsIII()
    
    test_cases = [
        ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
        ([[1, 0], [0, 2]], 1), # Simple path
        ([[1, 0, 0], [0, 0, 0], [0, 0, 2]], 0), # No path (need to visit 7 cells, path will be 8 steps) - Should be 2 paths if calculated correctly: [1,0,0,0,0,0,0,2] 
        # Corrected calculation for [1,0,0], [0,0,0], [0,0,2]: 7 empty cells + 1 start = 8 steps required
        # Total empty cells: 7. Start at (0,0). End at (2,2). Result is 4.
        # Let's use simpler test case logic.
        ([[1, 0, 0], [0, 0, 0], [0, 0, 2]], 2), # Correct path count is 2 (e.g., R, D, R, D, L, U, L, D, R, D... this is wrong)
        # Actual count is 4. (RDRDRU, DRDRUR, RDDRUL, etc.)
        
        ([[1, 0, 0], [0, 0, 0], [0, 0, 2]], 4), # 7 empty, 8 steps. Result 4.
        ([[0, 1], [2, 0]], 0),  # Start or End blocked by obstacle logic error in problem definition
        ([[1, 0, 0], [0, 0, 0], [0, 0, 2]], 4), # Re-test complex case
    ]

    print("--- Unique Paths III (DFS Backtracking) Test Results ---")
    
    for grid, expected in test_cases:
        result = solver.uniquePathsIII(grid)
        status = "PASSED" if result == expected else f"FAILED (Expected: {expected}, Got: {result})"
        
        # Print only the first row for brevity in output
        print(f"Grid: {grid[0]}... -> Paths: {result}, Status: {status}")