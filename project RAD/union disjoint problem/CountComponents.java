import java.util.*;

class UnionFind {
    int[] parent;
    int[] rank;
    int count; // number of components

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        count = n;

        // Initially, each node is its own parent
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    // Find operation with path compression
    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    // Union operation with rank optimization
    public boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY)
            return false; // already in the same group

        // Union by rank
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }

        count--; // One less component after merging
        return true;
    }
}

public class CountComponents {
    public static int countComponents(int n, int[][] edges) {
        UnionFind uf = new UnionFind(n);

        for (int[] edge : edges) {
            uf.union(edge[0], edge[1]);
        }

        return uf.count;
    }

    public static void main(String[] args) {
        int[][][] edgeCases = {
                { { 0, 1 }, { 1, 2 }, { 3, 4 } },
                { { 0, 1 }, { 1, 2 }, { 2, 3 }, { 3, 4 } },
                { { 0, 1 }, { 2, 3 } },
                { { 0, 1 }, { 2, 3 }, { 4, 5 }, { 0, 5 } },
                {}
        };
        int[] nodes = { 5, 5, 4, 6, 3 };
        int[] expected = { 2, 1, 2, 2, 3 };

        System.out.println("--- Number of Connected Components (Union-Find) Test Results ---");
        for (int i = 0; i < nodes.length; i++) {
            int result = countComponents(nodes[i], edgeCases[i]);
            String status = (result == expected[i])
                    ? "PASSED"
                    : "FAILED (Expected: " + expected[i] + ", Got: " + result + ")";
            System.out.println("Nodes: " + nodes[i] +
                    ", Components: " + result + ", Status: " + status);
        }
    }
}
