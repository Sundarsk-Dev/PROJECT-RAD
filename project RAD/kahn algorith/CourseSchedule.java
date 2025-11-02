import java.util.*;

public class CourseSchedule {
    public static boolean canFinish(int numCourses, int[][] prerequisites) {
        // 1. Create graph (Adjacency list)
        Map<Integer, List<Integer>> graph = new HashMap<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<>());
        }

        // Build graph and compute in-degree
        for (int[] pair : prerequisites) {
            int course = pair[0];
            int prereq = pair[1];
            graph.get(prereq).add(course);
            inDegree[course]++;
        }

        // 2. Initialize Queue with courses having in-degree 0
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }

        int finishedCount = 0;

        // 3. Process the queue (BFS)
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            finishedCount++;

            for (int neighbor : graph.get(curr)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // 4. Check if all courses are finished
        return finishedCount == numCourses;
    }

    public static void main(String[] args) {
        int[][][] testCases = {
                { { 1, 0 } }, // True
                { { 1, 0 }, { 0, 1 } }, // False
                { { 1, 0 }, { 2, 0 }, { 3, 1 }, { 3, 2 } }, // True
                { { 1, 0 }, { 2, 1 }, { 0, 2 } }, // False
                {} // True
        };
        int[] courseCounts = { 2, 2, 4, 3, 1 };
        boolean[] expected = { true, false, true, false, true };

        System.out.println("--- Course Schedule (Kahn's Algorithm) ---");
        for (int i = 0; i < testCases.length; i++) {
            boolean result = canFinish(courseCounts[i], testCases[i]);
            System.out.printf("Test %d: %s (Expected: %s)%n", i + 1, result, expected[i]);
        }
    }
}
