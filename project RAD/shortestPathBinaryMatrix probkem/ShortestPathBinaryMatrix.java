import java.util.*;

public class ShortestPathBinaryMatrix {

    public static int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;

        // 1. Initial checks
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1)
            return -1;
        if (n == 1)
            return 1;

        // 2. Directions: 8 possible moves
        int[][] directions = {
                { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 },
                { 1, 1 }, { 1, -1 }, { -1, 1 }, { -1, -1 }
        };

        // 3. BFS queue: store {row, col, distance}
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] { 0, 0, 1 });
        grid[0][0] = 1; // mark visited

        // 4. BFS traversal
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1], d = cell[2];

            // Goal check
            if (r == n - 1 && c == n - 1)
                return d;

            // Explore all 8 directions
            for (int[] dir : directions) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nc >= 0 && nr < n && nc < n && grid[nr][nc] == 0) {
                    queue.offer(new int[] { nr, nc, d + 1 });
                    grid[nr][nc] = 1; // mark as visited
                }
            }
        }

        // 5. No path found
        return -1;
    }

    public static void main(String[] args) {
        int[][][] testCases = {
                { { 0, 1 }, { 1, 0 } },
                { { 0, 0, 0 }, { 1, 1, 0 }, { 1, 1, 0 } },
                { { 1, 0, 0 }, { 1, 1, 0 }, { 1, 1, 0 } },
                { { 0 } },
                { { 0, 0, 0 }, { 1, 0, 0 }, { 1, 1, 0 } }
        };

        int[] expected = { 2, 4, -1, 1, 3 };

        for (int i = 0; i < testCases.length; i++) {
            int result = shortestPathBinaryMatrix(copyGrid(testCases[i]));
            System.out.printf("Test %d → Result: %d | Expected: %d | %s\n",
                    i + 1, result, expected[i],
                    (result == expected[i]) ? "PASSED" : "FAILED");
        }
    }

    // Utility to copy grid (since Java passes arrays by reference)
    private static int[][] copyGrid(int[][] grid) {
        int[][] newGrid = new int[grid.length][];
        for (int i = 0; i < grid.length; i++) {
            newGrid[i] = grid[i].clone();
        }
        return newGrid;
    }
}
