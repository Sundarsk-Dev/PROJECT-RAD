import java.util.*;

public class ShortestPathAllKeys {

    static class State {
        int r, c, mask, dist;

        State(int r, int c, int mask, int dist) {
            this.r = r;
            this.c = c;
            this.mask = mask;
            this.dist = dist;
        }
    }

    public int shortestPathAllKeys(String[] grid) {
        int m = grid.length, n = grid[0].length();
        int startR = 0, startC = 0, totalKeys = 0;

        // 1️⃣ Find start position and total keys
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                char ch = grid[r].charAt(c);
                if (ch == '@') {
                    startR = r;
                    startC = c;
                } else if (ch >= 'a' && ch <= 'f') {
                    totalKeys++;
                }
            }
        }

        int targetMask = (1 << totalKeys) - 1;
        int[][] directions = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        // 2️⃣ BFS Setup
        Queue<State> queue = new ArrayDeque<>();
        queue.offer(new State(startR, startC, 0, 0));

        Set<String> visited = new HashSet<>();
        visited.add(startR + "," + startC + "," + 0);

        // 3️⃣ BFS Loop
        while (!queue.isEmpty()) {
            State cur = queue.poll();

            if (cur.mask == targetMask)
                return cur.dist;

            for (int[] dir : directions) {
                int nr = cur.r + dir[0];
                int nc = cur.c + dir[1];
                int newMask = cur.mask;

                // Boundary + Wall Check
                if (nr < 0 || nc < 0 || nr >= m || nc >= n)
                    continue;
                char cell = grid[nr].charAt(nc);
                if (cell == '#')
                    continue;

                // Key Check
                if (cell >= 'a' && cell <= 'f') {
                    int keyBit = cell - 'a';
                    newMask = cur.mask | (1 << keyBit);
                }

                // Lock Check
                if (cell >= 'A' && cell <= 'F') {
                    int lockBit = cell - 'A';
                    if ((cur.mask & (1 << lockBit)) == 0)
                        continue;
                }

                String newState = nr + "," + nc + "," + newMask;
                if (!visited.contains(newState)) {
                    visited.add(newState);
                    queue.offer(new State(nr, nc, newMask, cur.dist + 1));
                }
            }
        }

        return -1;
    }

    // --- Test Cases ---
    public static void main(String[] args) {
        ShortestPathAllKeys solver = new ShortestPathAllKeys();

        String[][] tests = {
                { "@.a.#", "###.#", "b.A.B" },
                { "@..aA", "..B#.", "....b" },
                { "@Aa" },
                { "@.a..", "#.###", "b.#.B" }
        };
        int[] expected = { 8, 10, -1, -1 };

        for (int i = 0; i < tests.length; i++) {
            int result = solver.shortestPathAllKeys(tests[i]);
            System.out.println("Test " + (i + 1) + " -> Result: " + result +
                    " (Expected: " + expected[i] + ")");
        }
    }
}
