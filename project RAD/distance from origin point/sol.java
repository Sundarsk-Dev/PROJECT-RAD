import java.util.*;

public class sol {

    public static int[][] kClosest(int[][] points, int K) {
        // Max-Heap (store farthest point on top)
        // Each element = [distanceSquared, x, y]
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
                (a, b) -> Integer.compare(b[0], a[0]) // sort in descending order by distance
        );

        for (int[] point : points) {
            int x = point[0];
            int y = point[1];
            int distSq = x * x + y * y;

            // Add to heap
            maxHeap.offer(new int[] { distSq, x, y });

            // If heap size > K, remove the farthest point
            if (maxHeap.size() > K) {
                maxHeap.poll();
            }
        }

        // Prepare result array
        int[][] result = new int[K][2];
        int i = 0;
        while (!maxHeap.isEmpty()) {
            int[] entry = maxHeap.poll();
            result[i][0] = entry[1];
            result[i][1] = entry[2];
            i++;
        }

        return result;
    }

    public static void main(String[] args) {
        // --- Test Cases ---
        int[][][] testPoints = {
                { { 1, 3 }, { -2, 2 } },
                { { 3, 3 }, { 5, -1 }, { -2, 4 } },
                { { 6, 1 }, { 1, 6 }, { 2, 5 } },
                { { 1, 1 }, { 1, 1 } }
        };

        int[] Ks = { 1, 2, 2, 1 };

        System.out.println("--- K Closest Points to Origin Test Results ---");
        for (int t = 0; t < testPoints.length; t++) {
            int[][] result = kClosest(testPoints[t], Ks[t]);

            // Sort for easy comparison
            Arrays.sort(result, (a, b) -> {
                if (a[0] != b[0])
                    return Integer.compare(a[0], b[0]);
                return Integer.compare(a[1], b[1]);
            });

            System.out.print("Input: " + Arrays.deepToString(testPoints[t]));
            System.out.println(", K = " + Ks[t]);
            System.out.println("Result: " + Arrays.deepToString(result));
            System.out.println();
        }
    }
}
