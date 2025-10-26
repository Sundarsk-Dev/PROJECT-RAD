public class NumberOfIslands {

    private int rows, cols;
    private int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0)
            return 0;

        rows = grid.length;
        cols = grid[0].length;
        int islandCount = 0;

        // Scan every cell
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    islandCount++;
                    sinkIslandDFS(grid, r, c);
                }
            }
        }

        return islandCount;
    }

    private void sinkIslandDFS(char[][] grid, int r, int c) {
        // Base case: out of bounds
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == '0') {
            return;
        }

        // Mark as visited
        grid[r][c] = '0';

        // Visit 4 directions
        for (int[] dir : directions) {
            sinkIslandDFS(grid, r + dir[0], c + dir[1]);
        }
    }

    // --- Test Cases ---
    public static void main(String[] args) {
        NumberOfIslands solver = new NumberOfIslands();

        char[][] grid1 = {
                { '1', '1', '1', '1', '0' },
                { '1', '1', '0', '1', '0' },
                { '1', '1', '0', '0', '0' },
                { '0', '0', '0', '0', '0' }
        };
        System.out.println("Test 1 (Single Island): " + solver.numIslands(grid1) + " (Expected: 1)");

        char[][] grid2 = {
                { '1', '1', '0', '0', '0' },
                { '1', '1', '0', '0', '0' },
                { '0', '0', '1', '0', '0' },
                { '0', '0', '0', '1', '1' }
        };
        System.out.println("Test 2 (Multiple Islands): " + solver.numIslands(grid2) + " (Expected: 3)");
    }
}
