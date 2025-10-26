from typing import List

class NumberOfIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        # Directions: Up, Down, Left, Right
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Outer loops to check every cell
        for r in range(m):
            for c in range(n):
                # Found land ('1') that hasn't been sunk yet
                if grid[r][c] == '1':
                    island_count += 1
                    # Sink the entire connected island using DFS
                    self._sink_island_dfs(grid, m, n, r, c)
                    
        return island_count

    def _sink_island_dfs(self, grid: List[List[str]], m: int, n: int, r: int, c: int):
        """
        DFS utility to recursively mark all connected land cells as water ('0').
        """
        # Base Case 1: Out of bounds
        if not (0 <= r < m and 0 <= c < n):
            return
            
        # Base Case 2: Already water ('0') or already sunk/visited
        if grid[r][c] == '0':
            return

        # Action: Mark current cell as sunk/visited ('0')
        grid[r][c] = '0'

        # Recurse: Explore 4 neighbors
        for dr, dc in self.directions:
            self._sink_island_dfs(grid, m, n, r + dr, c + dc)

# --- Test Cases ---

if __name__ == "__main__":
    solver = NumberOfIslands()
    
    # Test Case 1: Single Island
    grid1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    expected1 = 1
    result1 = solver.numIslands(grid1)
    status1 = "PASSED" if result1 == expected1 else f"FAILED (Expected: {expected1}, Got: {result1})"
    print(f"Test 1 (Single Island) -> Islands: {result1}, Status: {status1}")

    # Test Case 2: Multiple Islands
    grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    expected2 = 3
    result2 = solver.numIslands(grid2)
    status2 = "PASSED" if result2 == expected2 else f"FAILED (Expected: {expected2}, Got: {result2})"
    print(f"Test 2 (Multiple Islands) -> Islands: {result2}, Status: {status2}")