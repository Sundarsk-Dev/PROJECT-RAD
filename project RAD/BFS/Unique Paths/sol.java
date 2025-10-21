class UniquePathsIII {

    private int totalRequiredSteps; // total cells to be visited (start + empty)
    private int pathCount; // total valid paths found
    private int[][] grid;
    private int m, n;

    // Directions (up, down, left, right)
    private final int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

    public int uniquePathsIII(int[][] grid) {
        this.m = grid.length;
        this.n = grid[0].length;
        this.grid = grid;
        int startRow = 0, startCol = 0;
        int emptyCells = 0;

        // 1️⃣ Find start position and count empty cells
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    startRow = r;
                    startCol = c;
                } else if (grid[r][c] == 0) {
                    emptyCells++;
                }
            }
        }

        // We must walk over all empty cells + start
        this.totalRequiredSteps = emptyCells + 1;
        this.pathCount = 0;

        // 2️⃣ Start DFS traversal
        dfs(startRow, startCol, 0);

        return pathCount;
    }

    private void dfs(int r, int c, int visitedCount) {
        // 3️⃣ Base case: Out of bounds or obstacle
        if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == -1) {
            return;
        }

        // 4️⃣ Base case: Reached end
        if (grid[r][c] == 2) {
            if (visitedCount == totalRequiredSteps) {
                pathCount++;
            }
            return;
        }

        // Save current cell value
        int original = grid[r][c];

        // Mark as visited
        grid[r][c] = -1;

        // Explore neighbors
        for (int[] dir : directions) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            dfs(nr, nc, visitedCount + 1);
        }

        // 5️⃣ Backtrack: Restore cell
        grid[r][c] = original;
    }

    // --- Test Cases ---
    public static void main(String[] args) {
        UniquePathsIII solver = new UniquePathsIII();

        int[][] grid1 = {
                { 1, 0, 0, 0 },
                { 0, 0, 0, 0 },
                { 0, 0, 2, -1 }
        };
        System.out.println("Paths: " + solver.uniquePathsIII(grid1) + " (Expected: 2)");

        int[][] grid2 = {
                { 1, 0 },
                { 0, 2 }
        };
        System.out.println("Paths: " + solver.uniquePathsIII(grid2) + " (Expected: 1)");

        int[][] grid3 = {
                { 1, 0, 0 },
                { 0, 0, 0 },
                { 0, 0, 2 }
        };
        System.out.println("Paths: " + solver.uniquePathsIII(grid3) + " (Expected: 4)");
    }
}
